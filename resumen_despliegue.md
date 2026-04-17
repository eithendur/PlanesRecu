# Resumen de Despliegue - Planes de Recuperación CIFP Avilés

---

## Servidor Requerido

| Componente | Versión mínima |
|-----------|---------------|
| SO | Linux (Ubuntu/Debian/CentOS) |
| PHP | 8.1+ |
| Apache | 2.4+ |
| Extensiones PHP | php-xml, php-zip, php-openssl, php-mbstring |
| Composer | Sí |

---

## Instalación

```bash
# 1. Subir archivos al servidor (ftp/scp/rsync)
# 2. composer install
# 3. chmod -R 775 logs/ uploads/
# 4. chown -R www-data:www-data PlanesDistancia/
# 5. systemctl restart apache2
```

---

## Requisitos del Proyecto

- No requiere base de datos.
- No requiere servicios adicionales.
- Solo PHP + Apache.

---

## Estructura de Archivos

```
PlanesDistancia/
├── app/                    # Aplicación completa
│   ├── index.html          # Panel principal
│   ├── procesar.php       # Procesamiento
│   ├── clases/           # Clases PHP
│   ├── assets/           # CSS, JS, imágenes
│   └── manual/           # Manuales PDF
├── logs/                  # Logs (permisos escritura)
├── uploads/               # Subidas (permisos escritura)
├── vendor/               # Dependencias Composer
├── resumen_despliegue.pdf  # Este resumen
└── Plantilla.xlsx         # Plantilla Excel
```

---

## Configuración SMTP

| Parámetro | Valor |
|----------|-------|
| Servidor | smtp.office365.com |
| Puerto | 587 |
| Cifrado | STARTTLS |
| Autenticación | Sí |
| Usuario | correo@educastur.org |
| Contraseña | Se introduce en el formulario |

---

## Notas

- El directorio `tests/` es solo para pruebas locales - NO subir al servidor.
- Los logs se guardan automáticamente en `logs/`.
- Los correos fallidos se guardan en `logs/YYYY-MM-DD/`.
- La aplicación pide la contraseña de correo en el formulario.

---

CIFP Avilés - Centro Integrado de Formación Profesional