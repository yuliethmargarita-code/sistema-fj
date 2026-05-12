from errores import ClienteError

class Cliente:

    def __init__(self, nombre, correo):

        if not nombre:
            raise ClienteError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__correo}"
