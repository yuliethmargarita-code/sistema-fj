from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva

print("=== SISTEMA SOFTWARE FJ ===")


# OPERACIÓN 1
try:
    cliente1 = Cliente("Laura", "laura@gmail.com")
    servicio1 = ReservaSala("Sala VIP", 100)

    reserva1 = Reserva(cliente1, servicio1, 2)
    reserva1.confirmar()

    print(reserva1.mostrar_reserva())

except Exception as e:
    print("Error:", e)


# OPERACIÓN 2
try:
    cliente2 = Cliente("", "correo@gmail.com")

except Exception as e:
    print("Error cliente:", e)


# OPERACIÓN 3
try:
    cliente3 = Cliente("Pedro", "correo_malo")

except Exception as e:
    print("Error correo:", e)


# OPERACIÓN 4
try:
    servicio2 = AlquilerEquipo("Computador Gamer", 200)

    print(
        "Costo alquiler:",
        servicio2.calcular_costo()
    )

except Exception as e:
    print("Error servicio:", e)


# OPERACIÓN 5
try:
    servicio3 = AsesoriaEspecializada(
        "Asesoría Empresarial",
        -50
    )

except Exception as e:
    print("Error precio:", e)


# OPERACIÓN 6
try:
    cliente4 = Cliente(
        "María",
        "maria@gmail.com"
    )

    servicio4 = ReservaSala(
        "Sala Reuniones",
        150
    )

    reserva2 = Reserva(
        cliente4,
        servicio4,
        -3
    )

except Exception as e:
    print("Error reserva:", e)


# OPERACIÓN 7
try:
    cliente5 = Cliente(
        "Carlos",
        "carlos@gmail.com"
    )

    servicio5 = AsesoriaEspecializada(
        "Consultoría",
        300
    )

    reserva3 = Reserva(
        cliente5,
        servicio5,
        5
    )

    reserva3.cancelar()

    print(reserva3.mostrar_reserva())

except Exception as e:
    print("Error:", e)


finally:
    print("\nPrograma finalizado correctamente")
