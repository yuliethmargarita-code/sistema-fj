import logging
from errores import ReservaError, SoftwareFJError

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
        Implementa el procesamiento con los tres tipos de bloques de excepción:
        try/except, try/except/else y try/except/finally (Requisito de la guía).
        También aplica encadenamiento de excepciones con 'raise from'.
        """
        try:
            # Calculamos el costo usando el método polimórfico del servicio
            costo = self.servicio.calcular_costo(self.duracion)

        except SoftwareFJError as e:
            self.estado = "Fallida"
            # Registro en el archivo de logs (Requisito: cada error debe registrarse)
            logging.error(f"Error procesando reserva para {self.cliente.get_nombre()}: {e}")
            # Encadenamiento de excepciones (Requisito de la guía)
            raise ReservaError(f"No se pudo completar la reserva: {e}") from e

        except Exception as e:
            # Captura cualquier otro error inesperado para mantener la estabilidad
            logging.error(f"Error inesperado en sistema: {e}")
            raise ReservaError("Error crítico en el procesamiento.") from e

        else:
            # Bloque else: solo se ejecuta si NO hubo ninguna excepción en el try
            # Aquí confirmamos la reserva porque el costo se calculó sin problemas
            self.confirmar()
            return f"Reserva PROCESADA: {self.mostrar_reserva()} | Costo Total: ${costo}"

        finally:
            # Bloque finally: siempre se ejecuta, haya error o no
            # Se usa para registrar que se intentó procesar la reserva
            logging.error(f"Intento de procesamiento registrado para: {self.cliente.get_nombre()}")

    def mostrar_reserva(self):
        # Usamos el nombre del servicio y la info del cliente
        return (
            f"{self.cliente.mostrar_info()} | "
            f"Servicio: {self.servicio.nombre_servicio} | "
            f"Estado: {self.estado}"
        )
