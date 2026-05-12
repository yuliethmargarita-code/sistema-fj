from abc import ABC, abstractmethod
from errores import ServicioError

class Servicio(ABC):
    """Clase abstracta Servicio (Requisito POO)"""
    def __init__(self, nombre_servicio, precio_base):
        # Validación estricta de parámetros (Requisito de robustez)
        if precio_base <= 0:
            raise ServicioError("El precio base debe ser un valor positivo.")
        
        self.nombre_servicio = nombre_servicio
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        """Método abstracto para implementar polimorfismo"""
        pass

# --- IMPLEMENTACIÓN DE POLIMORFISMO (3 Servicios Especializados) ---

class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioError("Las horas de reserva deben ser mayores a 0.")
        return self.precio_base * horas

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        if dias <= 0:
            raise ServicioError("Los días de alquiler deben ser mayores a 0.")
        # Simulación de un cargo fijo por seguro del equipo
        cargo_seguro = 15000 
        return (self.precio_base * dias) + cargo_seguro

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones):
        if sesiones <= 0:
            raise ServicioError("El número de sesiones debe ser mayor a 0.")
        # Sobrecarga lógica: Si son más de 5 sesiones, se aplica un 10% de descuento
        subtotal = self.precio_base * sesiones
        if sesiones > 5:
            return subtotal * 0.90
        return subtotal
