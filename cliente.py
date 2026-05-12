from abc import ABC, abstractmethod
from errores import ClienteError, SoftwareFJError
# Se importan las excepciones desde errores.py para no duplicar código

# Clase abstracta base del sistema
class EntidadBase(ABC):
    """Clase abstracta general que representa cualquier entidad del sistema"""
    @abstractmethod
    def mostrar_info(self):
        pass

# Clase Cliente con encapsulación y validaciones estrictas
class Cliente(EntidadBase):
    """Clase Cliente con encapsulación y validaciones estrictas"""
    def __init__(self, nombre, correo):
        if not nombre or len(nombre.strip()) == 0:
            raise ClienteError("El nombre no puede estar vacío.")
        if "@" not in correo:
            raise ClienteError(f"Correo inválido: {correo}")

        self.__nombre = nombre  # Encapsulamiento: atributo privado
        self.__correo = correo  # Encapsulamiento: atributo privado

    def get_nombre(self):
        return self.__nombre

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Email: {self.__correo}"
