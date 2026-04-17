import os
import pytest
from pathlib import Path

BASE_DIR = Path("C:/Users/ignaf/OneDrive/Documentos/Mis documentos/IA/Proyectos/PlanesDistancia")

class TestEstructura:
    
    def test_directorio_existe(self):
        assert BASE_DIR.exists(), "Debe existir el directorio base"
    
    def test_directorio_app_existe(self):
        app_dir = BASE_DIR / "app"
        assert app_dir.exists(), "Debe existir el directorio app"
    
    def test_directorio_clases_existe(self):
        clases_dir = BASE_DIR / "app" / "clases"
        assert clases_dir.exists(), "Debe existir el directorio clases"
    
    def test_directorio_assets_existe(self):
        assets_dir = BASE_DIR / "app" / "assets"
        assert assets_dir.exists(), "Debe existir el directorio assets"
    
    def test_directorio_css_existe(self):
        css_dir = BASE_DIR / "app" / "assets" / "css"
        assert css_dir.exists(), "Debe existir el directorio css"
    
    def test_directorio_js_existe(self):
        js_dir = BASE_DIR / "app" / "assets" / "js"
        assert js_dir.exists(), "Debe existir el directorio js"
    
    def test_directorio_manual_existe(self):
        manual_dir = BASE_DIR / "app" / "manual"
        assert manual_dir.exists(), "Debe existir el directorio manual"
    
    def test_directorio_logs_existe(self):
        logs_dir = BASE_DIR / "logs"
        assert logs_dir.exists(), "Debe existir el directorio logs"
    
    def test_directorio_errores_existe(self):
        errores_dir = BASE_DIR / "logs" / "errores"
        assert errores_dir.exists(), "Debe existir el directorio errores"
    
    def test_directorio_tests_existe(self):
        tests_dir = BASE_DIR / "tests"
        assert tests_dir.exists(), "Debe existir el directorio tests"

class TestFicheros:
    
    def test_index_html_existe(self):
        index_file = BASE_DIR / "app" / "index.html"
        assert index_file.exists(), "Debe existir index.html"
    
    def test_procesar_php_existe(self):
        procesar_file = BASE_DIR / "app" / "procesar.php"
        assert procesar_file.exists(), "Debe existir procesar.php"
    
    def test_css_existe(self):
        css_file = BASE_DIR / "app" / "assets" / "css" / "estilo.css"
        assert css_file.exists(), "Debe existir estilo.css"
    
    def test_js_existe(self):
        js_file = BASE_DIR / "app" / "assets" / "js" / "main.js"
        assert js_file.exists(), "Debe existir main.js"
    
    def test_logo_existe(self):
        logo_file = BASE_DIR / "app" / "assets" / "logo.jpg"
        assert logo_file.exists(), "Debe existir logo.jpg"
    
    def test_logger_php_existe(self):
        logger_file = BASE_DIR / "app" / "clases" / "Logger.php"
        assert logger_file.exists(), "Debe existir Logger.php"
    
    def test_errorhandler_php_existe(self):
        errorhandler_file = BASE_DIR / "app" / "clases" / "ErrorHandler.php"
        assert errorhandler_file.exists(), "Debe existir ErrorHandler.php"
    
    def test_excelreader_php_existe(self):
        excelreader_file = BASE_DIR / "app" / "clases" / "ExcelReader.php"
        assert excelreader_file.exists(), "Debe existir ExcelReader.php"
    
    def test_emailsender_php_existe(self):
        emailsender_file = BASE_DIR / "app" / "clases" / "EmailSender.php"
        assert emailsender_file.exists(), "Debe existir EmailSender.php"
    
    def test_manual_usuario_pdf_existe(self):
        manual_file = BASE_DIR / "app" / "manual" / "manual_usuario.pdf"
        assert manual_file.exists(), "Debe existir manual_usuario.pdf"
    
    def test_manual_despliegue_pdf_existe(self):
        manual_file = BASE_DIR / "app" / "manual" / "manual_despliegue.pdf"
        assert manual_file.exists(), "Debe existir manual_despliegue.pdf"

class TestContenido:
    
    def test_index_tiene_formulario(self):
        index_file = BASE_DIR / "app" / "index.html"
        contenido = index_file.read_text(encoding='utf-8')
        assert 'formulario' in contenido.lower(), "index.html debe contener formulario"
    
    def test_index_tiene_campos_tutor(self):
        index_file = BASE_DIR / "app" / "index.html"
        contenido = index_file.read_text(encoding='utf-8')
        assert 'tutor' in contenido.lower(), "index.html debe contener campo tutor"
    
    def test_index_tiene_email(self):
        index_file = BASE_DIR / "app" / "index.html"
        contenido = index_file.read_text(encoding='utf-8')
        assert 'email' in contenido.lower(), "index.html debe contener campo email"
    
    def test_index_tiene_directorio(self):
        index_file = BASE_DIR / "app" / "index.html"
        contenido = index_file.read_text(encoding='utf-8')
        assert 'directorio' in contenido.lower(), "index.html debe contener directorio"
    
    def test_index_tiene_excel(self):
        index_file = BASE_DIR / "app" / "index.html"
        contenido = index_file.read_text(encoding='utf-8')
        assert 'excel' in contenido.lower(), "index.html debe contener excel"
    
    def test_index_tiene_footer(self):
        index_file = BASE_DIR / "app" / "index.html"
        contenido = index_file.read_text(encoding='utf-8')
        assert 'copyright' in contenido.lower(), "index.html debe contener footer copyright"
    
    def test_css_tiene_colores_cifp(self):
        css_file = BASE_DIR / "app" / "assets" / "css" / "estilo.css"
        contenido = css_file.read_text(encoding='utf-8')
        assert '#1a3a6e' in contenido, "CSS debe contener color azul CIFP"
    
    def test_js_tiene_enviar(self):
        js_file = BASE_DIR / "app" / "assets" / "js" / "main.js"
        contenido = js_file.read_text(encoding='utf-8')
        assert 'enviar' in contenido.lower() or 'submit' in contenido.lower(), "JS debe manejar envio"

if __name__ == '__main__':
    result = pytest.main([__file__, '-v', '--tb=short'])
    exit(result)