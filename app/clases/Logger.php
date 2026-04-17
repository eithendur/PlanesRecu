<?php

class Logger {
    private string $logPath;
    private string $today;

    public function __construct(string $logPath) {
        $this->logPath = rtrim($logPath, '/\\');
        $this->today = date('Y-m-d');

        if (!is_dir($this->logPath)) {
            mkdir($this->logPath, 0755, true);
        }
    }

    private function getLogFile(): string {
        return $this->logPath . '/app_' . $this->today . '.log';
    }

    public function escribir(string $nivel, string $mensaje, array $contexto = []): void {
        $timestamp = date('Y-m-d H:i:s');
        $contextoStr = empty($contexto) ? '' : ' | ' . json_encode($contexto, JSON_UNESCAPED_UNICODE);
        $logLine = "[{$timestamp}] [{$nivel}] {$mensaje}{$contextoStr}" . PHP_EOL;

        file_put_contents($this->getLogFile(), $logLine, FILE_APPEND | LOCK_EX);
    }

    public function info(string $mensaje, array $contexto = []): void {
        $this->escribir('INFO', $mensaje, $contexto);
    }

    public function error(string $mensaje, array $contexto = []): void {
        $this->escribir('ERROR', $mensaje, $contexto);
    }

    public function warning(string $mensaje, array $contexto = []): void {
        $this->escribir('WARNING', $mensaje, $contexto);
    }

    public function getLogFiles(): array {
        $files = glob($this->logPath . '/app_*.log');
        return $files ?: [];
    }
}