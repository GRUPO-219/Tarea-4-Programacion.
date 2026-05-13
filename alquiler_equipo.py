from modelos.servicio import Servicio

class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):

        return (self.tarifa * horas) + 5000

    def descripcion(self):
        return "Servicio de alquiler de equipos"