from errores import ReservaError

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("Duración inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def mostrar_reserva(self):

        return (
            f"{self.cliente.mostrar_info()} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )
