
class Cliente:

    def __init__(self, nombre, cedula, correo):

        try:

            if nombre == "":
                print("El nombre está vacío")

            if not cedula.isdigit():
              print("querido usuario la cédula debe tener solo números")

            if "@" not in correo:
                print("Correo inválido")

            self.nombre = nombre
            self.cedula = cedula
            self.correo = correo

              guardar_log("el cliente es registrado correctamente")

        except Exception as error:

            guardar_log(f"Error al registrar cliente: {error}")

              print("A ocurrió un error:", error)

    def mostrar_info(self):
        return f"Cliente: {self.nombre} - Cédula: {self.cedula}"
