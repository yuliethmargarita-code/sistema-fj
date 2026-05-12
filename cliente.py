import logging
from abc import ABC, abstractmethod
from datetime import datetime

# ==========================================
# 1. MANEJO DE LOGS (Requisito: Registro de errores en archivo)
# ==========================================
logging.basicConfig(
    filename='software_fj_logs.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ==========================================
# 2. EXCEPCIONES PERSONALIZADAS
# ==========================================
class SoftwareFJError(Exception):
    """Clase base para errores del sistema"""
    pass

class ClienteError(SoftwareFJError):
    pass

class ServicioError(SoftwareFJError):
    pass

class ReservaError(SoftwareFJError):
    pass

# ==========================================
# 3. CLASES DE NEGOCIO (POO)
# ==========================================

class EntidadBase(ABC):
    """Clase abstracta general (Requisito)"""
    @abstractmethod
    def mostrar_info(self):
        pass

class Cliente(EntidadBase):
    """Clase Cliente con encapsulación y validaciones"""
    def __init__(self, nombre, correo):
        if not nombre or len(nombre.strip()) == 0:
            raise ClienteError("El nombre no puede estar vacío.")
        if "@" not in correo:
            raise ClienteError(f"Correo inválido: {correo}")
        
        self.__nombre = nombre  # Encapsulamiento
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Email: {self.__correo}"

class Servicio(ABC):
    """Clase abstracta Servicio"""
    def __init__(self, nombre_servicio):
        self.nombre_servicio = nombre_servicio

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

# --- POLIMORFISMO: 3 Servicios Especializados ---
class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0: raise ServicioError("Las horas deben ser positivas.")
        return horas * 50000  # Tarifa fija por hora

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        if dias <= 0: raise ServicioError("Los días deben ser positivos.")
        return dias * 30000  # Tarifa por día

class Asesoria(Servicio):
    def calcular_costo(self, sesiones):
        # Sobrecarga simulada mediante lógica de parámetros
        if sesiones <= 0: raise ServicioError("Sesiones inválidas.")
        base = sesiones * 80000
        return base * 0.9 if sesiones > 5 else base  # Descuento si son > 5

class Reserva:
    """Clase que integra Cliente y Servicio con manejo de excepciones"""
    def __init__(self, cliente, servicio, cantidad):
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "Pendiente"

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(self.cantidad)
            self.estado = "Confirmada"
            return f"Reserva de {self.servicio.nombre_servicio} para {self.cliente.get_nombre()} EXITOSA. Costo: ${costo}"
        except SoftwareFJError as e:
            self.estado = "Fallida"
            logging.error(f"Error en reserva: {e}")
            raise ReservaError(f"No se pudo procesar la reserva: {e}") from e

# ==========================================
# 4. SIMULACIÓN DE 10 OPERACIONES (Casos válidos e inválidos)
# ==========================================
def ejecutar_pruebas():
    print("--- INICIANDO SIMULACIÓN DE SOFTWARE FJ ---")
    
    # Listas para simular nuestra "base de datos" temporal
    clientes = []
    servicios = [ReservaSala("Sala VIP"), AlquilerEquipo("Laptop Pro"), Asesoria("Consultoría IT")]
    
    # 1. Crear Cliente Válido
    try:
        c1 = Cliente("Mateo", "mateo@correo.com")
        clientes.append(c1)
        print("Op 1: Cliente creado correctamente.")
    except Exception as e: logging.error(e)

    # 2. Intentar crear Cliente Inválido (Nombre vacío)
    try:
        c2 = Cliente("", "error@test.com")
    except ClienteError as e:
        logging.error(f"Op 2 (Fallo esperado): {e}")
        print(f"Op 2: Error controlado - {e}")

    # 3. Intentar crear Cliente Inválido (Correo sin @)
    try:
        c3 = Cliente("Juan", "juan-correo.com")
    except ClienteError as e:
        logging.error(f"Op 3 (Fallo esperado): {e}")
        print(f"Op 3: Error controlado - {e}")

    # 4. Reserva de Sala Exitosa
    try:
        res1 = Reserva(clientes[0], servicios[0], 4)
        print(f"Op 4: {res1.procesar()}")
    except Exception as e: print(e)

    # 5. Reserva de Sala Fallida (Horas negativas)
    try:
        res2 = Reserva(clientes[0], servicios[0], -2)
        print(f"Op 5: {res2.procesar()}")
    except ReservaError as e:
        print(f"Op 5: {e}")

    # 6. Alquiler de Equipo Exitoso
    try:
        res3 = Reserva(clientes[0], servicios[1], 3)
        print(f"Op 6: {res3.procesar()}")
    except Exception as e: print(e)

    # 7. Asesoría con Descuento (Más de 5 sesiones)
    try:
        res4 = Reserva(clientes[0], servicios[2], 10)
        print(f"Op 7: {res4.procesar()} (Aplicó descuento)")
    except Exception as e: print(e)

    # 8. Intento de Reserva con Parámetro No Permitido (Sesiones 0)
    try:
        res5 = Reserva(clientes[0], servicios[2], 0)
        print(f"Op 8: {res5.procesar()}")
    except ReservaError as e:
        print(f"Op 8: {e}")

    # 9. Crear otro cliente y hacer reserva válida
    try:
        c4 = Cliente("Lucia", "lucia@web.com")
        res6 = Reserva(c4, servicios[1], 1)
        print(f"Op 9: {res6.procesar()}")
    except Exception as e: print(e)

    # 10. Prueba de bloque Finally
    try:
        print("Op 10: Ejecutando verificación final del sistema...")
        if len(clientes) > 0:
            print(f"Resumen: Sistema estable con {len(clientes)} clientes registrados.")
    finally:
        print("Simulación finalizada. Revisa 'software_fj_logs.txt' para ver los errores registrados.")

if __name__ == "__main__":
    ejecutar_pruebas()
