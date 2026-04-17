from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate(
    "C:/Users/ignaf/OneDrive/Documentos/Mis documentos/IA/Proyectos/PlanesDistancia/app/manual/manual_migracion.pdf",
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

story.append(Paragraph("Manual de Migracion", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("Planes de Recuperacion - CIFP Aviles", normal_style))
story.append(Spacer(1, 0.5*inch))

story.append(Paragraph("1. Estrcutura de Archivos", heading_style))
story.append(Paragraph("Para desplegar en el servidor, subir la siguiente estructura:", normal_style))

data = [
    ['Carpeta/Archivo', 'Descripcion'],
    ['app/', 'Carpeta principal de la aplicacion'],
    ['app/index.html', 'Panel principal'],
    ['app/procesar.php', 'Procesamiento deenvios'],
    ['app/clases/', 'Clases PHP (Logger, ErrorHandler, etc.)'],
    ['app/assets/', 'CSS, JS, imagenes'],
    ['app/manual/', 'Manuales PDF'],
    ['logs/', 'Logs (permisos de escritura)'],
    ['uploads/', 'Subidas temporales (permisos)'],
    ['vendor/', 'Dependencias Composer']
]
t = Table(data, colWidths=[2*inch, 4*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1a3a6e")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f5f5f5")),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
story.append(t)
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("2. Requisitos del Servidor", heading_style))
data2 = [
    ['Componente', 'Version Minima'],
    ['PHP', '8.1+'],
    ['Apache', '2.4+'],
    ['Extensiones PHP', 'php-xml, php-zip, php-openssl, php-mbstring']
]
t2 = Table(data2, colWidths=[2*inch, 3.5*inch])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1a3a6e")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f5f5f5")),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
story.append(t2)
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("3. Dependencias Composer", heading_style))
story.append(Paragraph("Ejecutar en el servidor:", normal_style))
story.append(Paragraph("composer install", normal_style))
story.append(Paragraph("O si no hay Composer:", normal_style))
story.append(Paragraph("composer require phpoffice/phpspreadsheet phpmailer/phpmailer", normal_style))
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("4. Permisos", heading_style))
story.append(Paragraph("chmod -R 775 logs/ uploads/", normal_style))
story.append(Paragraph("chown -R www-data:www-data PlanesDistancia/", normal_style))
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("5. Configuracion Apache", heading_style))
story.append(Paragraph("Apuntar DocumentRoot a PlanesDistancia/app", normal_style))
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("6. Configuracion SMTP (Office 365)", heading_style))
data3 = [
    ['Parametro', 'Valor'],
    ['Servidor', 'smtp.office365.com'],
    ['Puerto', '587'],
    ['Cifrado', 'STARTTLS'],
    ['Autenticacion', 'Si'],
    ['Usuario', 'correo@educastur.org'],
    ['Contrasena', 'Se introduce en el formulario']
]
t3 = Table(data3, colWidths=[2*inch, 3*inch])
t3.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1a3a6e")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f5f5f5")),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
story.append(t3)
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("7. Notas Importantes", heading_style))
story.append(Paragraph("- El directorio tests/ es solo para pruebas locales - NO subir al servidor", normal_style))
story.append(Paragraph("- Los logs se guardan automaticamente en logs/", normal_style))
story.append(Paragraph("- Los correos fallidos se guardan en logs/YYYY-MM-DD/", normal_style))
story.append(Paragraph("- La aplicacion pide contrasena de correo en el formulario", normal_style))
story.append(Spacer(1, 0.5*inch))

story.append(Paragraph("CIFP Aviles - Centro Integrado de Formacion Profesional", normal_style))

doc.build(story)
print("PDF de migracion creado")