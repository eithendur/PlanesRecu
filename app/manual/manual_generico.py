from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate(
    "C:/Users/ignaf/OneDrive/Documentos/Mis documentos/IA/Proyectos/PlanesDistancia/app/manual/manual_generico.pdf",
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

story.append(Paragraph("Manual para Crear Planes Genéricos", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("Guía para generar documentos individuales desde una plantilla - CIFP Avilés", normal_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("1. Introducción", heading_style))
story.append(Paragraph("Este manual describe cómo crear planes de recuperación individuale"
                    "s usando la función de combinación de correspondencia de LibreOffice Writer."
                    " El proceso permite generar un documento por cada alumno desde una plantilla base.", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("2. Preparar los Datos", heading_style))
story.append(Paragraph("2.1 Crear Hoja de Cálculo", normal_style))
story.append(Paragraph("1. Abra Calc (LibreOffice) o Excel", normal_style))
story.append(Paragraph("2. Cree una hoja con los siguientes campos:", normal_style))

data = [
    ['Campo', 'Descripción', 'Ejemplo'],
    ['Nombre', 'Nombre completo del alumno', 'Juan García López'],
    ['Correo', 'Correo institucional', 'juan.garcia@educastur.org'],
    ['Curso', 'Curso del alumno', '1ºDAM'],
    ['Módulo', 'Módulo formativo', 'Programación']
]
t = Table(data, colWidths=[1.5*inch, 2.5*inch, 2*inch])
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
story.append(Paragraph("3. Guarde el archivo como datos.ods (formato ODF)", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("3. Crear la Plantilla", heading_style))
story.append(Paragraph("3.1 Diseño del Documento", normal_style))
story.append(Paragraph("1. Abra LibreOffice Writer", normal_style))
story.append(Paragraph("2. Cree un nuevo documento en blanco", normal_style))
story.append(Paragraph("3. Diseñe la plantilla con el siguiente contenido:", normal_style))
story.append(Paragraph("- Datos del centro (encabezado)", normal_style))
story.append(Paragraph("- Título del documento", normal_style))
story.append(Paragraph("- Datos del alumno (nombre, curso, módulo)", normal_style))
story.append(Paragraph("- Contenido del plan", normal_style))
story.append(Paragraph("- Firma del profesor", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("3.2 Insertar Campos de Combinación", normal_style))
story.append(Paragraph("Ir al menú \"Archivo\", \"Imprimir\".", normal_style))
story.append(Paragraph("Aparecerá ventana indicando si se quiere imprimir una carta modelo, damos a \"Sí\".", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Aparece la ventana \"Combinación de correspondencia\" donde se ve la tabla con los datos.", normal_style))
story.append(Paragraph("Como salida elegimos \"Archivo\" y \"Separar en documentos individuales\".", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Escoger el campo que va a dar nombre a los archivos.", normal_style))
story.append(Paragraph("Los archivos generados pueden ser en distintos formatos, por defecto usará el ODF.", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("ODF (Open Document Format) es un formato de archivo que incluye a los archivos ODT,"
                    " que son documentos de procesamiento de texto. ODF es un estándar internacional de archivos XML.", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("4. Ejecutar la Combinación", heading_style))
story.append(Paragraph("4.1 Seleccionar Origen de Datos", normal_style))
story.append(Paragraph("1. Vaya a \"Ver\" → \"Origen de datos\" o presione F4", normal_style))
story.append(Paragraph("2. Seleccione la hoja de cálculo con los datos", normal_style))
story.append(Paragraph("3. Los campos aparecerán en el panel lateral", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("4.2 Insertar Campos en la Plantilla", normal_style))
story.append(Paragraph("1. Pulse en la posición donde desea insertar un campo", normal_style))
story.append(Paragraph("2. Arrastre el campo desde el panel lateral", normal_style))
story.append(Paragraph("3. Repita para cada campo necesario", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("4.3 Generar Documentos", normal_style))
story.append(Paragraph("1. Vaya a \"Editar\" → \"Buscar y reemplazar\"", normal_style))
story.append(Paragraph("2. En \"Buscar\" escriba el nombre del campo entre < >", normal_style))
story.append(Paragraph("3. Use \"替换todo\" para reemplazarlos todos", normal_style))
story.append(Paragraph("4. Guarde cada documento con el nombre del alumno", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("5. Opciones de Exportación", heading_style))

data2 = [
    ['Formato', 'Extensión', 'Descripción'],
    ['ODF', 'ODT', 'Formato estándar abierto (recomendado)'],
    ['PDF', 'PDF', 'Formato portable de Adobe'],
    ['DOC', 'DOC', 'Compatible con Word (legacy)'],
    ['DOCX', 'DOCX', 'Formato Word moderno']
]
t2 = Table(data2, colWidths=[1*inch, 1*inch, 2.5*inch])
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
story.append(Paragraph("6. Consejos", heading_style))
story.append(Paragraph("- Use nombres descriptivos en la plantilla", normal_style))
story.append(Paragraph("- Verifique los datos antes de generar", normal_style))
story.append(Paragraph("- Genere primero un documento de prueba", normal_style))
story.append(Paragraph("- Guarde los documentos en una carpeta organizada", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("7. Resolución de Problemas", heading_style))

data3 = [
    ['Problema', 'Solución'],
    ['Campos no aparecen', 'Verificar que la hoja de cálculo está abierta'],
    ['Documentos vacíos', 'Comprobar que los campos están bien escritos'],
    ['Error al guardar', 'Verificar permisos de la carpeta de destino']
]
t3 = Table(data3, colWidths=[2.5*inch, 3*inch])
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
story.append(Paragraph("8. Contacto", heading_style))
story.append(Paragraph("Para soporte técnico, contacte con el administrador del sistema.", normal_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("Manual actualizado: Abril 2025", normal_style))
story.append(Paragraph("CIFP Avilés - Centro Integrado de Formación Profesional", normal_style))

doc.build(story)