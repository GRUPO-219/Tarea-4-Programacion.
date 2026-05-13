from modelos.servicio import Servicio

class Asesoria(Servicio):

    def calcular_costo(self, horas):

        return (self.tarifa * horas) * 1.19

    def descripcion(self):
        return "Servicio de asesoría especializada"