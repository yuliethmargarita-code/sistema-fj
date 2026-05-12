from errores import ReservaError, SoftwareFJError
import logging

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        # Validación estricta (Requisito de la guía)
        if duracion <= 0:
            raise ReservaError("La duración de la reserva debe ser mayor a cero.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar_reserva(self):
        """
        Implementa el procesamiento con manejo de excepciones y registro en logs.
        """
        try:
            # Calculamos el costo usando el método polimórfico del servicio
            costo = self.servicio.calcular_costo(self.duracion)
            self.confirmar()
            return f"Reserva PROCESADA: {self.mostrar_reserva()} | Costo Total: ${costo}"
        
        except SoftwareFJError as e:
            self.estado = "Fallida"
            # Registro en el archivo de logs (Requisito: cada error debe registrarse)
            logging.error(f"Error procesando reserva para {self.cliente.get_nombre()}: {e}")
            raise ReservaError(f"No se pudo completar la reserva: {e}")
        
        except Exception as e:
            # Captura cualquier otro error inesperado para mantener la estabilidad
            logging.error(f"Error inesperado en sistema: {e}")
            raise ReservaError("Error crítico en el procesamiento.")

    def mostrar_reserva(self):
        # Usamos el nombre del servicio y la info del cliente
        return (
            f"{self.cliente.mostrar_info()} | "
            f"Servicio: {self.servicio.nombre_servicio} | "
            f"Estado: {self.estado}"
        )
