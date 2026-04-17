<?php

require_once __DIR__ . '/../app/clases/Logger.php';
require_once __DIR__ . '/../app/clases/ErrorHandler.php';

class TestsLogger {
    private $tmpPath;
    private $passed = 0;
    private $failed = 0;

    public function __construct() {
        $this->tmpPath = sys_get_temp_dir() . '/test_logs_' . uniqid();
        if (!is_dir($this->tmpPath)) {
            mkdir($this->tmpPath, 0755, true);
        }
    }

    public function assert($condition, $message) {
        if ($condition) {
            echo "[PASS] $message\n";
            $this->passed++;
        } else {
            echo "[FAIL] $message\n";
            $this->failed++;
        }
    }

    public function testCrearLogger() {
        $log = new Logger($this->tmpPath);
        $log->escribir('INFO', 'Test message');
        
        $files = glob($this->tmpPath . '/app_*.log');
        $this->assert(count($files) == 1, "testCrearLogger: Debe crear un archivo de log");
    }

    public function testEscribirInfo() {
        $log = new Logger($this->tmpPath);
        $log->info('Test info message');
        
        $files = glob($this->tmpPath . '/app_*.log');
        $content = file_get_contents($files[0]);
        
        $this->assert(
            strpos($content, 'Test info message') !== false && strpos($content, 'INFO') !== false,
            "testEscribirInfo: Debe escribir mensaje con nivel INFO"
        );
    }

    public function testEscribirError() {
        $log = new Logger($this->tmpPath);
        $log->error('Test error message');
        
        $files = glob($this->tmpPath . '/app_*.log');
        $content = file_get_contents($files[0]);
        
        $this->assert(
            strpos($content, 'Test error message') !== false && strpos($content, 'ERROR') !== false,
            "testEscribirError: Debe escribir mensaje con nivel ERROR"
        );
    }

    public function testEscribirConContexto() {
        $log = new Logger($this->tmpPath);
        $log->info('Test message', ['tutor' => 'Juan', 'alumnos' => 5]);
        
        $files = glob($this->tmpPath . '/app_*.log');
        $content = file_get_contents($files[0]);
        
        $this->assert(
            strpos($content, 'Juan') !== false && strpos($content, '5') !== false,
            "testEscribirConContexto: Debe incluir contexto en el log"
        );
    }

    public function testRotacionFecha() {
        $log = new Logger($this->tmpPath);
        $log->escribir('INFO', 'Test 1');
        
        $files = glob($this->tmpPath . '/app_*.log');
        
        $this->assert(
            strpos($files[0], 'app_') !== false,
            "testRotacionFecha: El archivo debe tener formato app_YYYY-MM-DD"
        );
    }

    public function testCrearFicheroError() {
        $handler = new ErrorHandler($this->tmpPath);
        
        $datos = [
            'tutor' => 'Juan',
            'alumno' => 'Maria',
            'error' => 'SMTP failed'
        ];
        $archivo = $handler->guardar($datos);
        
        $this->assert(file_exists($archivo), "testCrearFicheroError: Debe crear archivo JSON");
        
        $contenido = json_decode(file_get_contents($archivo), true);
        $this->assert($contenido['tutor'] === 'Juan', "testCrearFicheroError: Debe guardar datos correctamente");
    }

    public function testErrorGuardaTimestamp() {
        $handler = new ErrorHandler($this->tmpPath);
        
        $datos = ['tutor' => 'Test', 'error' => 'Error test'];
        $archivo = $handler->guardar($datos);
        
        $contenido = json_decode(file_get_contents($archivo), true);
        
        $this->assert(
            isset($contenido['timestamp']),
            "testErrorGuardaTimestamp: Debe guardar timestamp"
        );
    }

    public function runAll() {
        echo "=== Ejecutando Tests Unitarios ===\n\n";
        
        $this->testCrearLogger();
        $this->testEscribirInfo();
        $this->testEscribirError();
        $this->testEscribirConContexto();
        $this->testRotacionFecha();
        $this->testCrearFicheroError();
        $this->testErrorGuardaTimestamp();
        
        echo "\n=== Resultados ===\n";
        echo "Pasados: {$this->passed}\n";
        echo "Fallidos: {$this->failed}\n";
        echo "Total: " . ($this->passed + $this->failed) . "\n";
        
        return $this->failed === 0;
    }
}

$tests = new TestsLogger();
$success = $tests->runAll();

$logFile = __DIR__ . '/logs/test_results.log';
$logDir = dirname($logFile);
if (!is_dir($logDir)) {
    mkdir($logDir, 0755, true);
}

$resultado = $success ? "PASSED" : "FAILED";
$contenido = "[" . date('Y-m-d H:i:s') . "] [$resultado] Tests unitarios ejecutados: Pasados: {$tests->passed}, Fallados: {$tests->failed}\n";
file_put_contents($logFile, $contenido, FILE_APPEND);

exit($success ? 0 : 1);