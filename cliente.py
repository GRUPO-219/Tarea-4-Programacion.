class cliente:
    def __init__(self, nombre, cedula, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo

    def mostrar_info(self):
        return f"cliente: {self.nombre} - Cédula: {self.cedula} - Correo: {self.correo}"


def guardar_log(mensaje):
    with open("logs_sistema.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")