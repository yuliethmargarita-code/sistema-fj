from abc import ABC, abstractmethod
from errores import ServicioError

class Servicio(ABC):

    def __init__(self, nombre, precio):

        if precio <= 0:
            raise ServicioError("El precio debe ser mayor a 0")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self):
        return self.precio * 2


class AlquilerEquipo(Servicio):

    def calcular_costo(self):
        return self.precio * 3


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self):
        return self.precio * 4
