import logging
from modelos.cliente import Cliente
from modelos.reserva import Reserva
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria

logging.basicConfig(
    filename='logs/sistema.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def ejecutar_pruebas():

    operaciones = []

    try:
        cliente1 = Cliente("Carlos", "carlos@gmail.com", "3124567890")
        servicio1 = ReservaSala("Sala Premium", 50000)
        reserva1 = Reserva(cliente1, servicio1, 2)

        costo = reserva1.procesar()

        operaciones.append(f"Reserva exitosa: {cliente1.get_nombre()} - ${costo}")

    except Exception as e:
        logging.error(f"Error operación 1: {e}")


    try:
        cliente2 = Cliente("", "correo_invalido", "abc")
        operaciones.append("Cliente inválido creado")

    except Exception as e:
        logging.error(f"Error operación 2: {e}")
        operaciones.append(f"Error controlado: {e}")


    try:
        cliente3 = Cliente("Ana", "ana@gmail.com", "3001234567")
        servicio2 = AlquilerEquipo("Portátiles", 30000)
        reserva2 = Reserva(cliente3, servicio2, 3)

        costo = reserva2.procesar()

        operaciones.append(f"Reserva exitosa: {cliente3.get_nombre()} - ${costo}")

    except Exception as e:
        logging.error(f"Error operación 3: {e}")


    try:
        cliente4 = Cliente("Luis", "luis@gmail.com", "3100000000")
        servicio3 = Asesoria("Asesoría IA", 80000)
        reserva3 = Reserva(cliente4, servicio3, -1)

        reserva3.procesar()

    except Exception as e:
        logging.error(f"Error operación 4: {e}")
        operaciones.append(f"Error controlado: {e}")


    print("\n===== RESULTADOS =====")

    for op in operaciones:
        print(op)

    print("\nEl sistema sigue funcionando correctamente.")

if __name__ == "__main__":
    ejecutar_pruebas()