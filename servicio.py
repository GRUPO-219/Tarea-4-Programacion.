from abc import ABC, abstractmethod
from modelos.entidad import Entidad

class Servicio(Entidad):

    def __init__(self, nombre, tarifa):

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    def mostrar_info(self):
        return f"{self.nombre} - ${self.tarifa}"