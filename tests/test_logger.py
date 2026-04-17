import pytest
import os
import sys
import json
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'app' / 'clases'))

class TestLogger:
    
    def test_crear_logger(self, tmp_path):
        from Logger import Logger
        
        log = Logger(str(tmp_path))
        log.escribir('INFO', 'Test message')
        
        archivos = list(tmp_path.glob('app_*.log'))
        assert len(archivos) == 1, "Debe crear un archivo de log"
    
    def test_escribir_info(self, tmp_path):
        from Logger import Logger
        
        log = Logger(str(tmp_path))
        log.info('Test info message')
        
        archivos = list(tmp_path.glob('app_*.log'))
        assert len(archivos) == 1
        contenido = archivos[0].read_text()
        assert 'Test info message' in contenido
        assert 'INFO' in contenido
    
    def test_escribir_error(self, tmp_path):
        from Logger import Logger
        
        log = Logger(str(tmp_path))
        log.error('Test error message')
        
        archivos = list(tmp_path.glob('app_*.log'))
        contenido = archivos[0].read_text()
        assert 'Test error message' in contenido
        assert 'ERROR' in contenido
    
    def test_escribir_con_contexto(self, tmp_path):
        from Logger import Logger
        
        log = Logger(str(tmp_path))
        log.info('Test message', {'tutor': 'Juan', 'alumnos': 5})
        
        archivos = list(tmp_path.glob('app_*.log'))
        contenido = archivos[0].read_text()
        assert 'Juan' in contenido
        assert '5' in contenido
    
    def test_rotacion_fecha(self, tmp_path):
        from Logger import Logger
        
        log = Logger(str(tmp_path))
        log.escribir('INFO', 'Test 1')
        
        archivos = list(tmp_path.glob('app_*.log'))
        assert 'app_' in archivos[0].name

class TestErrorHandler:
    
    def test_crear_fichero_error(self, tmp_path):
        from ErrorHandler import ErrorHandler
        
        handler = ErrorHandler(str(tmp_path))
        
        datos = {
            'tutor': 'Juan',
            'alumno': 'Maria',
            'error': 'SMTP failed'
        }
        archivo = handler.guardar(datos)
        
        assert os.path.exists(archivo)
        contenido = json.loads(Path(archivo).read_text())
        assert contenido['tutor'] == 'Juan'
        assert contenido['alumno'] == 'Maria'
    
    def test_error_guarda_timestamp(self, tmp_path):
        from ErrorHandler import ErrorHandler
        
        handler = ErrorHandler(str(tmp_path))
        
        datos = {'tutor': 'Test', 'error': 'Error test'}
        archivo = handler.guardar(datos)
        
        contenido = json.loads(Path(archivo).read_text())
        assert 'timestamp' in contenido
    
    def test_get_errores(self, tmp_path):
        from ErrorHandler import ErrorHandler
        
        handler = ErrorHandler(str(tmp_path))
        
        handler.guardar({'tutor': 'Test1', 'error': 'Error 1'})
        handler.guardar({'tutor': 'Test2', 'error': 'Error 2'})
        
        errores = handler.getErrores()
        assert len(errores) == 2

if __name__ == '__main__':
    pytest.main([__file__, '-v'])