<?php

require_once __DIR__ . '/../../vendor/autoload.php';

use PhpOffice\PhpSpreadsheet\IOFactory;

class ExcelReader {
    private string $filePath;
    private array $data = [];

    public function __construct(string $filePath) {
        $this->filePath = $filePath;
    }

    public function leer(): array {
        if (!file_exists($this->filePath)) {
            throw new \Exception("El archivo Excel no existe: {$this->filePath}");
        }

        try {
            $spreadsheet = IOFactory::load($this->filePath);
            $sheet = $spreadsheet->getActiveSheet();
            $rows = $sheet->toArray();

            if (empty($rows)) {
                throw new \Exception("El archivo Excel está vacío");
            }

            $header = array_map('trim', array_map('strtolower', $rows[0]));

            $nombreIdx = $this->buscarIndice($header, ['nombre alumno', 'nombre_alumno', 'nombre', 'alumno']);
            $correoIdx = $this->buscarIndice($header, ['correo alumno', 'correo_alumno', 'correo', 'email']);
            $planIdx = $this->buscarIndice($header, ['plan', 'fichero', 'plan recuperacion']);

            if ($nombreIdx === null || $correoIdx === null || $planIdx === null) {
                throw new \Exception("El Excel debe contener columnas: Nombre Alumno, Correo Alumno, Plan");
            }

            for ($i = 1; $i < count($rows); $i++) {
                $row = $rows[$i];
                $nombre = trim($row[$nombreIdx] ?? '');
                $correo = trim($row[$correoIdx] ?? '');
                $plan = trim($row[$planIdx] ?? '');

                if (!empty($nombre) && !empty($correo) && !empty($plan)) {
                    $this->data[] = [
                        'nombre' => $nombre,
                        'correo' => $correo,
                        'plan' => $plan
                    ];
                }
            }

            return $this->data;
        } catch (\Exception $e) {
            throw new \Exception("Error al leer el Excel: " . $e->getMessage());
        }
    }

    private function buscarIndice(array $header, array $nombres): ?int {
        foreach ($nombres as $nombre) {
            $idx = array_search($nombre, $header);
            if ($idx !== false) {
                return $idx;
            }
        }
        return null;
    }

    public function getData(): array {
        return $this->data;
    }
}