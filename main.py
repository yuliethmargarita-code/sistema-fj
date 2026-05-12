import logging
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from errores import SoftwareFJError

# La configuración del log ya está en errores.py, no se repite aquí

print("=== SISTEMA INTEGRAL SOFTWARE FJ ===")

# OPERACIÓN 1: Registro Exitoso
try:
    c1 = Cliente("Laura", "laura@gmail.com")
    s1 = ReservaSala("Sala VIP", 100000)
    r1 = Reserva(c1, s1, 2)
    print(f"Op 1: {r1.procesar_reserva()}")
except Exception as e:
    logging.error(f"Error Op 1: {e}")

# OPERACIÓN 2: Cliente sin nombre (Error)
try:
    c2 = Cliente("", "correo@gmail.com")
except Exception as e:
    print(f"Op 2: Error capturado - {e}")
    logging.error(f"Error Op 2: {e}")

# OPERACIÓN 3: Correo inválido (Error)
try:
    c3 = Cliente("Pedro", "correo_malo")
except Exception as e:
    print(f"Op 3: Error capturado - {e}")
    logging.error(f"Error Op 3: {e}")

# OPERACIÓN 4: Alquiler de Equipo Exitoso
try:
    s2 = AlquilerEquipo("Computador Gamer", 50000)
    print(f"Op 4: Costo alquiler (3 días): {s2.calcular_costo(3)}")
except Exception as e:
    logging.error(f"Error Op 4: {e}")

# OPERACIÓN 5: Precio negativo en servicio (Error)
try:
    s3 = AsesoriaEspecializada("Asesoría Empresarial", -50)
except Exception as e:
    print(f"Op 5: Error capturado - {e}")
    logging.error(f"Error Op 5: {e}")

# OPERACIÓN 6: Reserva con duración negativa (Error)
try:
    c4 = Cliente("María", "maria@gmail.com")
    s4 = ReservaSala("Sala Reuniones", 150000)
    r2 = Reserva(c4, s4, -3)
    r2.procesar_reserva()
except Exception as e:
    print(f"Op 6: Error capturado - {e}")
    logging.error(f"Error Op 6: {e}")

# OPERACIÓN 7: Asesoría con Descuento (Exitoso)
try:
    c5 = Cliente("Carlos", "carlos@gmail.com")
    s5 = AsesoriaEspecializada("Consultoría IT", 200000)
    r3 = Reserva(c5, s5, 6)  # 6 sesiones aplica descuento
    print(f"Op 7: {r3.procesar_reserva()}")
except Exception as e:
    logging.error(f"Error Op 7: {e}")

# OPERACIÓN 8: Cancelación de reserva
try:
    r3.cancelar()
    print(f"Op 8: {r3.mostrar_reserva()}")
except Exception as e:
    logging.error(f"Error Op 8: {e}")

# OPERACIÓN 9: Parámetros de servicio inválidos (0 sesiones)
try:
    s6 = AsesoriaEspecializada("Ciberseguridad", 300000)
    print(f"Op 9: {s6.calcular_costo(0)}")
except Exception as e:
    print(f"Op 9: Error capturado - {e}")
    logging.error(f"Error Op 9: {e}")

# OPERACIÓN 10: Validación final de robustez
try:
    print("Op 10: Validando estado final del sistema...")
    c_final = Cliente("Mateo", "mateo@softwarefj.com")
    print(f"Sistema estable. Último cliente creado: {c_final.get_nombre()}")
except Exception as e:
    logging.error(f"Error Op 10: {e}")
finally:
    print("\nSimulación finalizada. Revisa 'software_fj_logs.txt' para ver los registros.")
