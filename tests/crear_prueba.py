from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(["Nombre Alumno", "Correo Alumno", "Plan"])
ws.append(["Juan García López", "juan.garcia@educastur.org", "plan_juan_garcia.pdf"])
ws.append(["María Fernández Smith", "maria.fernandez@educastur.org", "plan_maria_fernandez.pdf"])
ws.append(["Carlos Rodríguez Iglesias", "carlos.rodriguez@educastur.org", "plan_carlos_rodriguez.pdf"])

wb.save("C:/Users/ignaf/OneDrive/Documentos/Mis documentos/IA/Proyectos/PlanesDistancia/tests/datos_prueba.xlsx")
print("Excel de prueba actualizado con columnas correctas")