import logging

# Configuración del archivo de logs — solo se hace UNA vez aquí
# Así todos los archivos usan el mismo registro sin conflictos
logging.basicConfig(
    filename='software_fj_logs.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- EXCEPCIONES PERSONALIZADAS (Requisito: Manejo robusto de errores) ---
class SoftwareFJError(Exception):
    """Clase base para todas las excepciones del sistema Software FJ"""
    pass

class ClienteError(SoftwareFJError):
    """Excepción para errores relacionados con la clase Cliente"""
    pass

class ServicioError(SoftwareFJError):
    """Excepción para errores en los servicios (costos, parámetros)"""
    pass

class ReservaError(SoftwareFJError):
    """Excepción para errores en el procesamiento de reservas"""
    pass
