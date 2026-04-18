from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate(
    "C:/Users/ignaf/OneDrive/Documentos/Mis documentos/IA/Proyectos/PlanesDistancia/app/manual/manual_despliegue.pdf",
    pagesize=A4,
    rightMargin=72,
    leftMargin=72,
    topMargin=72,
    bottomMargin=72,
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    spaceAfter=30,
    textColor=colors.HexColor("#1a3a6e"),
    alignment=1
)
heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    spaceBefore=20,
    spaceAfter=10,
    textColor=colors.HexColor("#1a3a6e")
)
normal_style = ParagraphStyle(
    'CustomNormal',
    parent=styles['Normal'],
    fontSize=11,
    spaceAfter=10,
    alignment=0
)

story = []

story.append(Paragraph("Manual de Despliegue", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("Sistema PDF Multisender - CIFP Aviles", normal_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("1. Tecnologias Utilizadas", heading_style))
story.append(Paragraph("El sistema esta construido con las siguientes tecnologias:", normal_style))

data_tech = [
    ['Tecnologia', 'Tipo', 'Version', 'Descripcion'],
    ['PHP', 'Lenguaje', '8.1+', 'Lado del servidor'],
    ['HTML/CSS', 'Frontend', '-', 'Interfaz de usuario'],
    ['PHPMailer', 'Libreria', '6.9+', 'Envio de correos SMTP'],
    ['PHPSpreadsheet', 'Libreria', '1.29+', 'Lectura de archivos Excel'],
    ['Apache', 'Servidor', '2.4', 'Servidor web'],
    ['Composer', 'Gestor', '2.0+', 'Gestion de dependencias PHP'],
    ['ReportLab', 'Libreria', '-', 'Generacion de PDFs (Python)']
]
t_tech = Table(data_tech, colWidths=[1.8*inch, 1*inch, 1*inch, 2.2*inch])
t_tech.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#e85a19")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f5f5f5")),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
story.append(t_tech)
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("2. Introduccion", heading_style))
story.append(Paragraph("Este manual describe los pasos necesarios para desplegar la aplicacion en un servidor Apache con PHP.", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("3. Requisitos del Servidor", heading_style))

data = [
    ['Componente', 'Version Minima'],
    ['PHP', '8.1'],
    ['Apache', '2.4'],
    ['Extensiones PHP', 'php_xml, php_zip, php_openssl, php_mbstring']
]
t = Table(data, colWidths=[2.5*inch, 3.5*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1a3a6e")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f5f5f5")),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
story.append(t)
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("3. Estructura de Directorios", heading_style))
story.append(Paragraph("/var/www/html/", normal_style))
story.append(Paragraph("└── PlanesDistancia/", normal_style))
story.append(Paragraph("    ├── app/", normal_style))
story.append(Paragraph("    │   ├── clases/", normal_style))
story.append(Paragraph("    │   ├── assets/", normal_style))
story.append(Paragraph("    │   └── manual/", normal_style))
story.append(Paragraph("    ├── logs/", normal_style))
story.append(Paragraph("    │   └── errores/", normal_style))
story.append(Paragraph("    └── vendor/", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("4. Instalacion", heading_style))
story.append(Paragraph("4.1 Preparacion del Entorno", normal_style))
story.append(Paragraph("# Crear directorio de aplicacion", normal_style))
story.append(Paragraph("mkdir -p /var/www/html/PlanesDistancia", normal_style))
story.append(Paragraph("cd /var/www/html/PlanesDistancia", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("4.2 Instalacion de Dependencias", normal_style))
story.append(Paragraph("Si no existe el directorio vendor/, ejecutar:", normal_style))
story.append(Paragraph("# Instalar Composer", normal_style))
story.append(Paragraph("curl -sS https://getcomposer.org/installer | php", normal_style))
story.append(Paragraph("mv composer.phar /usr/local/bin/composer", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("# Instalar todas las dependencias (PHPSpreadsheet + PHPMailer)", normal_style))
story.append(Paragraph("composer install", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Opcional: instalar manualmente:", normal_style))
story.append(Paragraph("composer require phpoffice/phpspreadsheet", normal_style))
story.append(Paragraph("composer require phpmailer/phpmailer", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("4.3 Permisos", normal_style))
story.append(Paragraph("# Establecer permisos", normal_style))
story.append(Paragraph("chown -R www-data:www-data /var/www/html/PlanesDistancia", normal_style))
story.append(Paragraph("chmod -R 755 /var/www/html/PlanesDistancia", normal_style))
story.append(Paragraph("chmod -R 775 /var/www/html/PlanesDistancia/logs", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("4.4 Configuracion de Apache", normal_style))
story.append(Paragraph("<VirtualHost *:80>", normal_style))
story.append(Paragraph("    ServerName planes.cifpaviles.net", normal_style))
story.append(Paragraph("    DocumentRoot /var/www/html/PlanesDistancia/app", normal_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("    <Directory /var/www/html/PlanesDistancia/app>", normal_style))
story.append(Paragraph("        Options -Indexes +FollowSymLinks", normal_style))
story.append(Paragraph("        AllowOverride All", normal_style))
story.append(Paragraph("        Require all granted", normal_style))
story.append(Paragraph("    </Directory>", normal_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("    ErrorLog ${APACHE_LOG_DIR}/planes_error.log", normal_style))
story.append(Paragraph("    CustomLog ${APACHE_LOG_DIR}/planes_access.log", normal_style))
story.append(Paragraph("</VirtualHost>", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("4.5 Configuracion de PHP", normal_style))
story.append(Paragraph("En php.ini:", normal_style))
story.append(Paragraph("upload_max_filesize = 10M", normal_style))
story.append(Paragraph("post_max_size = 10M", normal_style))
story.append(Paragraph("max_execution_time = 300", normal_style))
story.append(Paragraph("max_input_time = 300", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("4.6 Reiniciar Apache", normal_style))
story.append(Paragraph("# En Debian/Ubuntu", normal_style))
story.append(Paragraph("systemctl restart apache2", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("5. En Windows (Desarrollo Local)", heading_style))
story.append(Paragraph("Para pruebas locales en Windows:", normal_style))
story.append(Paragraph("1. Descargar PHP 8.4 para Windows (VS17 x64)", normal_style))
story.append(Paragraph("2. Extraer y añadir al PATH:", normal_style))
story.append(Paragraph("   set PATH=%PATH%;C:\\php", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("3. Habilitar extensiones en php.ini:", normal_style))
story.append(Paragraph("   extension=openssl", normal_style))
story.append(Paragraph("   extension=mbstring", normal_style))
story.append(Paragraph("   extension=fileinfo", normal_style))
story.append(Paragraph("   extension=gd", normal_style))
story.append(Paragraph("   extension=zip", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("4. Instalar Composer:", normal_style))
story.append(Paragraph("   php -r \"copy('https://getcomposer.org/installer', 'composer-setup.php');\"", normal_style))
story.append(Paragraph("   php composer-setup.php --install-dir=. --filename=composer", normal_style))
story.append(Paragraph("   php composer install", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("5. Iniciar servidor:", normal_style))
story.append(Paragraph("   php -S localhost:8080 -t app", normal_style))
story.append(Paragraph("   O usar el archivo:", normal_style))
story.append(Paragraph("   start_server.bat", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("5. Configuracion SMTP", heading_style))
story.append(Paragraph("5.1 Servidor Educastur (Predeterminado)", normal_style))
story.append(Paragraph("El sistema esta configurado para usar smtp.educastur.org por defecto.", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("5.2 Servidores Alternativos", normal_style))
story.append(Paragraph("Si necesita usar otro servidor, marque la opcion 'Usar servidor SMTP alternativo' en el formulario.", normal_style))

data2 = [
    ['Servidor', 'Host', 'Puerto', 'Encryption'],
    ['Gmail', 'smtp.gmail.com', '587', 'TLS'],
    ['Outlook', 'smtp.office365.com', '587', 'TLS'],
    ['Yahoo', 'smtp.mail.yahoo.com', '587', 'TLS']
]
t2 = Table(data2, colWidths=[1.5*inch, 2*inch, 1*inch, 1*inch])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1a3a6e")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f5f5f5")),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
story.append(t2)
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("6. Verificacion", heading_style))
story.append(Paragraph("6.1 Pruebas Basico", normal_style))
story.append(Paragraph("1. Acceda a la URL de la aplicacion", normal_style))
story.append(Paragraph("2. Verifique que el logo CIFP se muestra", normal_style))
story.append(Paragraph("3. Verifique que el formulario carga", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("6.2 Pruebas de Envio", normal_style))
story.append(Paragraph("1. Prepare un Excel de prueba con 1-2 alumnos", normal_style))
story.append(Paragraph("2. Prepare PDFs de prueba", normal_style))
story.append(Paragraph("3. Realice un envio de prueba", normal_style))
story.append(Paragraph("4. Verifique que los correos llegan", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("7. Mantenimiento", heading_style))
story.append(Paragraph("7.1 Logs", normal_style))
story.append(Paragraph("Los logs se encuentran en: logs/app_YYYY-MM-DD.log - Log general", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("7.2 Errores", normal_style))
story.append(Paragraph("Los errores se guardan en: logs/errores/YYYY-MM-DD/error_*.json", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("7.3 Copias de Seguridad", normal_style))
story.append(Paragraph("Se recomienda incluir en la backup:", normal_style))
story.append(Paragraph("- Directorio logs/", normal_style))
story.append(Paragraph("- Ficheros de Excel usados", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("8. Seguridad", heading_style))
story.append(Paragraph("8.1 Recomendaciones", normal_style))
story.append(Paragraph("- Usar HTTPS en produccion", normal_style))
story.append(Paragraph("- Restringir acceso por IP si es posible", normal_style))
story.append(Paragraph("- Actualizar regularmente las dependencias", normal_style))
story.append(Paragraph("- Monitorizar los logs", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("9. Resolucion de Problemas", heading_style))

data3 = [
    ['Problema', 'Solucion'],
    ['Error 500', 'Verificar permisos y logs de PHP'],
    ['No envia correos', 'Verificar configuracion SMTP'],
    ['No lee Excel', 'Verificar extensiones PHP'],
    ['Timeout', 'Aumentar max_execution_time']
]
t3 = Table(data3, colWidths=[2.5*inch, 3.5*inch])
t3.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1a3a6e")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f5f5f5")),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
story.append(t3)
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("10. Contacto", heading_style))
story.append(Paragraph("Para soporte tecnico, contacte con el administrador del sistema.", normal_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("Manual actualizado: Abril 2025", normal_style))
story.append(Paragraph("CIFP Aviles - Centro Integrado de Formacion Profesional", normal_style))

doc.build(story)