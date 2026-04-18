# PDF Multisender - Planes, Boletines y Otros Documentos

Sistema de envío masivo de documentos PDF por correo electrónico para CIFP Avilés.

## Descripción

Aplicación web desarrollada en PHP que permite enviar documentos PDF de forma masiva a múltiples destinatarios leyendo los datos de un archivo Excel. Ideal para enviar planes de recuperación, boletines, certificados y otros documentos a estudiantes.

## Características

- 📧 Envío masivo de correos con adjuntos PDF
- 📊 Integración con Excel para datos de destinatarios
- 📎 Envío de copia al remitente (opcional)
- ⚙️ Soporte para servidores SMTP alternativos
- 📄 Generación de manuales en PDF
- 🎨 Interfaz con diseño CIFP Avilés

## Estructura del Proyecto

```
PlanesDistancia/
├── app/
│   ├── index.html          # Formulario principal
│   ├── procesar.php      # Lógica de procesamiento
│   ├── clases/
│   │   ├── EmailSender.php    # Envío de correos
│   │   ├── ExcelReader.php   # Lectura de Excel
│   │   ├── Logger.php      # Registro de logs
│   │   └── ErrorHandler.php # Manejo de errores
│   ├── assets/
│   │   ├── css/estilo.css
│   │   ├── js/main.js
│   │   └── logo.jpg
│   └── manual/
│       ├── manual_usuario.pdf
│       ├── manual_despliegue.pdf
│       └── manual_generico.pdf
├── tests/
│   └── planes/          # PDFs de prueba
├── logs/                # Logs de aplicación
├── uploads/             # Archivos subidos
├── composer.json
└── start_server.bat
```

## Requisitos

- PHP 8.1+
- Composer
- Extensiones PHP: php_xml, php_zip, php_openssl, php_mbstring

## Instalación

### 1. Instalar dependencias
```bash
composer install
```

### 2. Iniciar servidor
```bash
# Windows
start_server.bat

# Linux/Mac
php -S localhost:8080 -t app
```

### 3. Acceder
```
http://localhost:8080
```

## Uso del Formulario

1. **Nombre del Remitente**: Tu nombre completo
2. **Correo Electrónico**: Tu correo institucional (@educastur.org)
3. **Contraseña**: Contraseña de tu correo
4. **Cuerpo del Correo**: Mensaje que recibirán los destinatarios
5. **Ficheros PDF**: Selecciona los archivos PDF a enviar
6. **Fichero Excel**: Archivo con columnas: Nombre Alumno, Correo Alumno, Plan

### Excel: Estructura Requerida

| Nombre Alumno | Correo Alumno | Plan |
|--------------|---------------|------|
| Juan García | juan.garcia@educastur.org | plan_juan_garcia.pdf |
| María Fernández | maria.fernandez@educastur.org | plan_maria_fernandez.pdf |

## Opciones Adicionales

- **Reenviar una copia al destinatario**: Envía una copia del correo al remitente
- **Usar servidor SMTP alternativo**: Configurar otro servidor de correo

## Manuales

- 📄 **Manual de Usuario**: Guía de uso de la aplicación
- ⚙️ **Manual de Despliegue**: Instrucciones de instalación en servidor
- 📑 **Manual Genérico**: Cómo crear planes usando LibreOffice

## Tecnologías Utilizadas

| Tecnología | Tipo | Versión |
|------------|------|--------|
| PHP | Lenguaje | 8.1+ |
| HTML/CSS | Frontend | - |
| PHPMailer | Librería | 6.9+ |
| PHPSpreadsheet | Librería | 1.29+ |
| Apache | Servidor | 2.4 |
| Composer | Gestor deps. | 2.0+ |

## Configuración SMTP

| Servidor | Host | Puerto |
|----------|------|--------|
| Outlook/Office 365 | smtp.office365.com | 587 |
| Gmail | smtp.gmail.com | 587 |
| Yahoo | smtp.mail.yahoo.com | 587 |

## Licencia

Copyright © 2025-2026 CIFP Avilés - Centro Integrado de Formación Profesional

## Autor

Desarrollado para CIFP Avilés