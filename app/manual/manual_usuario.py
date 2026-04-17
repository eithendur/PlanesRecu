from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate(
    "C:/Users/ignaf/OneDrive/Documentos/Mis documentos/IA/Proyectos/PlanesDistancia/app/manual/manual_usuario.pdf",
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

story.append(Paragraph("Manual de Usuario", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("Sistema de Envio de Planes de Recuperacion - CIFP Aviles", normal_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("1. Introduccion", heading_style))
story.append(Paragraph("Este manual describe como utilizar el sistema de envio masivo de planes de recuperacion por correo electronico. El sistema permite a los tutores enviar planes de recuperacion a sus alumnos de forma automatica.", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("2. Requisitos Previos", heading_style))
story.append(Paragraph("- Navegador web actualizado (Chrome, Firefox, Edge)", normal_style))
story.append(Paragraph("- Fichero Excel con los datos de los alumnos", normal_style))
story.append(Paragraph("- Ficheros PDF con los planes de recuperacion", normal_style))
story.append(Paragraph("- Acceso a correo electronico institucional (@educastur.org)", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("3. Estructura del Fichero Excel", heading_style))
story.append(Paragraph("El fiche Excel debe contener las siguientes columnas en la primera fila:", normal_style))
story.append(Spacer(1, 0.2*inch))

data = [
    ['Columna', 'Descripcion', 'Ejemplo'],
    ['Nombre Alumno', 'Nombre completo del alumno', 'Juan Garcia Lopez'],
    ['Correo Alumno', 'Correo electronico del alumno', 'juan.garcia@educastur.org'],
    ['Plan', 'Nombre del fichier PDF', 'plan_juan_garcia.pdf']
]
t = Table(data, colWidths=[2*inch, 2.5*inch, 2*inch])
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
story.append(Paragraph("Importante: Los nombres de los PDFs deben coincidir exactamente con los indicados en la columna C.", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("4. Estructura de Directorio", heading_style))
story.append(Paragraph("Los fiche PDFs deben estar organizados en un directorio:", normal_style))
story.append(Paragraph("/planes/", normal_style))
story.append(Paragraph("├── plan_alumno1.pdf", normal_style))
story.append(Paragraph("├── plan_alumno2.pdf", normal_style))
story.append(Paragraph("└── plan_alumno3.pdf", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("5. Pasos para el Envio", heading_style))
story.append(Paragraph("5.1 Acceso a la Aplicacion", normal_style))
story.append(Paragraph("1. Abra el navegador web", normal_style))
story.append(Paragraph("2. Acceda a la URL de la aplicacion", normal_style))
story.append(Paragraph("3. Verifique que la pagina carga correctamente", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("5.2 Relleno del Formulario", normal_style))
story.append(Paragraph("1. Nombre del Tutor/a: Introduzca su nombre completo", normal_style))
story.append(Paragraph("2. Correo Electronico: Introduzca su correo institucional (@educastur.org)", normal_style))
story.append(Paragraph("3. Directorio de Ficheros PDF: Haga clic en 'Seleccionar' y elija el directorio que contiene los PDFs", normal_style))
story.append(Paragraph("4. Fichero Excel: Haga clic en 'Seleccionar' y elija el fiche Excel con los datos", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("5.3 Envio", normal_style))
story.append(Paragraph("1. Verifique que todos los campos muestran valores selecionados", normal_style))
story.append(Paragraph("2. Haga clic en 'ENVIAR PLANES'", normal_style))
story.append(Paragraph("3. Espere a que se complete el proceso", normal_style))
story.append(Paragraph("4. Se mostrara un mensaje con el resultado", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("6. Interpretacion de Resultados", heading_style))
story.append(Paragraph("6.1 Exito", normal_style))
story.append(Paragraph("- Todos los correos se enviaron correctamente", normal_style))
story.append(Paragraph("- Los alumnos recibiran el correo con el plan", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("6.2 Fallos", normal_style))
story.append(Paragraph("- Algunos correos no se pudieron enviar", normal_style))
story.append(Paragraph("- Los errores se guardan automaticamente", normal_style))
story.append(Paragraph("- Puede revisar los erros e intentar el reenvio manualmente", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("7. Solucion de Problemas", heading_style))
story.append(Paragraph("- No se selecciona el directorio: Use Chrome o Edge para mejor compatibilidad", normal_style))
story.append(Paragraph("- Error al leer el Excel: Verifique que el Excel tiene el formato correcto", normal_style))
story.append(Paragraph("- Correos no llegan: Revise la bandeja de spam", normal_style))
story.append(Paragraph("- Error de conexion SMTP: Marque 'Usar servidor SMTP alternativo' y configure", normal_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("8. Contacto de Soporte", heading_style))
story.append(Paragraph("Para incidencias tecnicas, contacte con el administrador del sistema.", normal_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("Manual actualizado: Abril 2025", normal_style))
story.append(Paragraph("CIFP Aviles - Centro Integrado de Formacion Profesional", normal_style))

doc.build(story)