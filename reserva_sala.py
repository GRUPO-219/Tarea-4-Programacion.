from modelos.servicio import Servicio

class ReservaSala(Servicio):

    def calcular_costo(self, horas, descuento=0):

        total = self.tarifa * horas
        return total - descuento

    def descripcion(self):
        return "Servicio de reserva de salas"