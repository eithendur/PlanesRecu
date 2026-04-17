<?php

class ErrorHandler {
    private string $errorPath;
    private string $today;

    public function __construct(string $errorPath) {
        $this->errorPath = rtrim($errorPath, '/\\');
        $this->today = date('Y-m-d');
    }

    private function getErrorDir(): string {
        $dir = $this->errorPath . '/' . $this->today;
        if (!is_dir($dir)) {
            mkdir($dir, 0755, true);
        }
        return $dir;
    }

    public function guardar(array $datos): string {
        $datos['timestamp'] = date('Y-m-d H:i:s');
        $filename = $this->getErrorDir() . '/error_' . time() . '_' . uniqid() . '.json';
        file_put_contents($filename, json_encode($datos, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE), LOCK_EX);
        return $filename;
    }

    public function getErrores(): array {
        $dir = $this->errorPath;
        if (!is_dir($dir)) {
            return [];
        }

        $errors = [];
        $subdirs = glob($dir . '/*', GLOB_ONLYDIR);

        foreach ($subdirs as $subdir) {
            $files = glob($subdir . '/*.json');
            foreach ($files as $file) {
                $content = file_get_contents($file);
                $errors[] = json_decode($content, true);
            }
        }

        return $errors;
    }
}