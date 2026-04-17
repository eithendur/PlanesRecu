from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate(
    "C:/Users/ignaf/OneDrive/Documentos/Mis documentos/IA/Proyectos/PlanesDistancia/resumen_despliegue.pdf",
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
    fontSize=28,
    spaceAfter=30,
    textColor=colors.HexColor("#000000"),
    alignment=1
)
heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    spaceBefore=20,
    spaceAfter=10,
    textColor=colors.HexColor("#000000")
)
normal_style = ParagraphStyle(
    'CustomNormal',
    parent=styles['Normal'],
    fontSize=12,
    spaceAfter=10,
    alignment=0
)
code_style = ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontSize=10,
    fontName='Courier',
    spaceAfter=5,
    alignment=0
)

story = []

story.append(Paragraph("RESUMEN DE DESPLIEGUE", title_style))
story.append(Paragraph("Planes de Recuperacion - CIFP Aviles", normal_style))
story.append(Spacer(1, 0.5*inch))

story.append(Paragraph("SERVIDOR REQUERIDO", heading_style))
data = [
    ['Componente', 'Version minima'],
    ['SO', 'Linux (Ubuntu/Debian/CentOS)'],
    ['PHP', '8.1+'],
    ['Apache', '2.4+'],
    ['Extensiones PHP', 'php-xml, php-zip, php-openssl, php-mbstring'],
    ['Composer', 'Si']
]
t = Table(data, colWidths=[2.5*inch, 3*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#000000")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f0f0f0")),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
story.append(t)
story.append(Spacer(1, 0.5*inch))

story.append(Paragraph("INSTALACION", heading_style))
story.append(Paragraph("1. Subir archivos al servidor (ftp/scp/rsync)", normal_style))
story.append(Paragraph("2. composer install", code_style))
story.append(Paragraph("3. chmod -R 775 logs/ uploads/", code_style))
story.append(Paragraph("4. chown -R www-data:www-data PlanesDistancia/", code_style))
story.append(Paragraph("5. systemctl restart apache2", code_style))
story.append(Spacer(1, 0.5*inch))

story.append(Paragraph("ESO ES TODO.", heading_style))
story.append(Paragraph("No requiere base de datos.", normal_style))
story.append(Paragraph("No requiere servicios adicionales.", normal_style))
story.append(Paragraph("Solo PHP + Apache.", normal_style))
story.append(Spacer(1, 1*inch))

story.append(Paragraph("CIFP Aviles - Centro Integrado de Formacion Profesional", normal_style))

doc.build(story)
print("PDF creado: resumen_despliegue.pdf")