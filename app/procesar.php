<?php

error_reporting(E_ALL);
ini_set('display_errors', 0);

require_once __DIR__ . '/clases/ExcelReader.php';
require_once __DIR__ . '/clases/EmailSender.php';
require_once __DIR__ . '/clases/Logger.php';
require_once __DIR__ . '/clases/ErrorHandler.php';

header('Content-Type: application/json');

$basePath = dirname(__DIR__);
$logsPath = $basePath . '/logs';

$logger = new Logger($logsPath);
$errorHandler = new ErrorHandler($logsPath);

function respuesta($success, $message, $data = []) {
    echo json_encode(array_merge([
        'success' => $success,
        'message' => $message
    ], $data));
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    respuesta(false, 'Método no permitido');
}

$tutor = trim($_POST['tutor'] ?? '');
$emailTutor = trim($_POST['email_tutor'] ?? '');

if (empty($tutor) || empty($emailTutor)) {
    respuesta(false, 'Por favor, complete todos los campos obligatorios');
}

if (!filter_var($emailTutor, FILTER_VALIDATE_EMAIL)) {
    respuesta(false, 'El correo electrónico del tutor no es válido');
}

$smtpCustom = !empty($_POST['smtp_custom']);
$smtpHost = $_POST['smtp_host'] ?? 'smtp.office365.com';
$smtpUser = $_POST['smtp_user'] ?: $emailTutor;
$smtpPass = $_POST['password'] ?? ($_POST['smtp_pass'] ?? '');

if (!isset($_FILES['excel']) || $_FILES['excel']['error'] !== UPLOAD_ERR_OK) {
    respuesta(false, 'Error al subir el archivo Excel');
}

if (!isset($_FILES['pdfs']) || empty($_FILES['pdfs']['name'][0])) {
    respuesta(false, 'Por favor, seleccione los PDFs');
}

$excelTmp = $_FILES['excel']['tmp_name'];
$excelName = $_FILES['excel']['name'];
$uploadDir = $basePath . '/uploads';

if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0755, true);
}

$excelPath = $uploadDir . '/' . time() . '_' . $excelName;
move_uploaded_file($excelTmp, $excelPath);

$directorioPath = $uploadDir . '/pdfs_' . time();

if (!is_dir($directorioPath)) {
    mkdir($directorioPath, 0755, true);
}

$pdfFiles = $_FILES['pdfs'];
$tmpFiles = $pdfFiles['tmp_name'] ?? [];
$fileNames = $pdfFiles['name'] ?? [];

for ($i = 0; $i < count($tmpFiles); $i++) {
    $tmpFile = $tmpFiles[$i] ?? '';
    $fileName = $fileNames[$i] ?? 'file.pdf';
    if ($tmpFile && is_uploaded_file($tmpFile)) {
        move_uploaded_file($tmpFile, $directorioPath . '/' . $fileName);
    }
}

$logger->info('Inicio', ['tutor' => $tutor, 'excel' => $excelName, 'pdfs' => count($tmpFiles)]);

try {
    $reader = new ExcelReader($excelPath);
    $alumnos = $reader->leer();

    if (empty($alumnos)) {
        respuesta(false, 'El Excel no contiene datos');
    }

    $emailSender = new EmailSender(
        $smtpCustom ? $smtpHost : 'smtp.office365.com',
        $smtpUser,
        $smtpPass
    );

    $exitos = 0;
    $fallos = 0;
    $errores = [];

    foreach ($alumnos as $alumno) {
        $nombreAlumno = $alumno['nombre'];
        $correoAlumno = $alumno['correo'];
        $planFile = $alumno['plan'];

        $pdfPath = $directorioPath . '/' . $planFile;

        try {
            if (!file_exists($pdfPath)) {
                throw new Exception("PDF no encontrado: $planFile");
            }

            $emailSender->enviar(
                $emailTutor,
                $tutor,
                $correoAlumno,
                $nombreAlumno,
                $pdfPath
            );

            $logger->info('Enviado', ['alumno' => $nombreAlumno, 'email' => $correoAlumno]);
            $exitos++;
        } catch (Exception $e) {
            $logger->error('Error', ['alumno' => $nombreAlumno, 'error' => $e->getMessage()]);

            $errorHandler->guardar([
                'tutor' => $tutor,
                'email_tutor' => $emailTutor,
                'alumno' => $nombreAlumno,
                'email_alumno' => $correoAlumno,
                'plan' => $planFile,
                'error' => $e->getMessage()
            ]);

            $fallos++;
            $errores[] = $nombreAlumno . ': ' . $e->getMessage();
        }
    }

    @unlink($excelPath);

    $logger->info('Fin', ['total' => count($alumnos), 'exitos' => $exitos, 'fallos' => $fallos]);

    respuesta(true, 'Completado', [
        'total' => count($alumnos),
        'exitos' => $exitos,
        'fallos' => $fallos,
        'errores' => $errores
    ]);
} catch (Exception $e) {
    $logger->error('Error proceso', ['error' => $e->getMessage()]);
    respuesta(false, $e->getMessage());
}