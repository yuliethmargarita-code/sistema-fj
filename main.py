from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo
from reserva import Reserva

try:

    cliente1 = Cliente("Laura", "laura@gmail.com")

    servicio1 = ReservaSala("Sala VIP", 100)

    reserva1 = Reserva(cliente1, servicio1, 2)

    reserva1.confirmar()

    print(reserva1.mostrar_reserva())

except Exception as e:
    print("Error:", e)

finally:
    print("Programa finalizado")
