<?php

require_once __DIR__ . '/../../vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

class EmailSender {
    private string $smtpHost;
    private string $smtpUser;
    private string $smtpPass;
    private int $smtpPort;

    private const SMTP_DEFAULT = 'smtp.office365.com';
    private const SMTP_PORT = 587;

    public function __construct(
        string $smtpHost = self::SMTP_DEFAULT,
        string $smtpUser = '',
        string $smtpPass = '',
        int $smtpPort = self::SMTP_PORT
    ) {
        $this->smtpHost = $smtpHost;
        $this->smtpUser = $smtpUser;
        $this->smtpPass = $smtpPass;
        $this->smtpPort = $smtpPort;
    }

    public function enviar(
        string $fromEmail,
        string $fromName,
        string $toEmail,
        string $alumno,
        string $attachmentPath,
        string $body = '',
        bool $enviarCopia = false
    ): bool {
        $mail = new PHPMailer(true);

        try {
            $mail->SMTPDebug = SMTP::DEBUG_OFF;
            $mail->isSMTP();
            $mail->Host = $this->smtpHost;
            $mail->SMTPAuth = true;
            $mail->Username = $this->smtpUser;
            $mail->Password = $this->smtpPass;
            $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
            $mail->Port = $this->smtpPort;
            $mail->CharSet = 'UTF-8';
            $mail->Timeout = 30;

            $mail->setFrom($fromEmail, $fromName);
            $mail->addAddress($toEmail);
            
            if ($enviarCopia) {
                $mail->addCC($fromEmail, $fromName);
            }

            $mail->Subject = $alumno;
            $mail->Body = $body ?: 'Se adjunta documento';
            $mail->isHtml(false);

            if (!empty($attachmentPath) && file_exists($attachmentPath)) {
                $mail->addAttachment($attachmentPath);
            } elseif (!empty($attachmentPath)) {
                throw new \Exception("Archivo no encontrado: {$attachmentPath}");
            }

            $mail->send();
            return true;
        } catch (Exception $e) {
            throw new \Exception("Error al enviar correo: " . $mail->ErrorInfo);
        }
    }
}