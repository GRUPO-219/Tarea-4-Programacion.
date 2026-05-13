from excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def procesar(self, descuento=0, impuesto=0):

        if self.horas <= 0:
            raise ReservaError("Horas inválidas")

        costo = self.servicio.calcular_costo(self.horas)

        costo -= costo * descuento
        costo += costo * impuesto

        self.estado = "Confirmada"
        return costo

    def cancelar(self):
        self.estado = "Cancelada"
