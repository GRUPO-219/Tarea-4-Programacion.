import logging
from modelos.cliente import Cliente
from modelos.reserva import Reserva
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria
from modelos.excepciones import ClienteInvalidoError, ReservaError, ServicioNoDisponibleError

logging.basicConfig(
    filename='logs/sistema.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def ejecutar_pruebas():
    operaciones = []

    # 1. Reserva exitosa de sala
    try:
        cliente1 = Cliente("Carlos", "carlos@gmail.com", "3124567890")
        servicio1 = ReservaSala("Sala Premium", 50000)
        reserva1 = Reserva(cliente1, servicio1, 2)
        costo = reserva1.procesar()
        operaciones.append(f"Reserva exitosa: {cliente1.get_nombre()} - ${costo}")
        logging.info("Reserva de sala confirmada correctamente")
    except Exception as e:
        logging.error(f"Error operación 1: {e}")

    # 2. Cliente inválido
    try:
        cliente2 = Cliente("", "correo_invalido", "abc")
        operaciones.append("Cliente inválido creado")
    except Exception as e:
        logging.error(f"Error operación 2: {e}")
        operaciones.append(f"Error controlado: {e}")

    # 3. Reserva exitosa de equipo
    try:
        cliente3 = Cliente("Ana", "ana@gmail.com", "3001234567")
        servicio2 = AlquilerEquipo("Portátiles", 30000)
        reserva2 = Reserva(cliente3, servicio2, 3)
        costo = reserva2.procesar()
        operaciones.append(f"Reserva exitosa: {cliente3.get_nombre()} - ${costo}")
        logging.info("Reserva de equipo confirmada correctamente")
    except Exception as e:
        logging.error(f"Error operación 3: {e}")

    # 4. Reserva fallida por duración negativa
    try:
        cliente4 = Cliente("Luis", "luis@gmail.com", "3100000000")
        servicio3 = Asesoria("Asesoría IA", 80000)
        reserva3 = Reserva(cliente4, servicio3, -1)
        reserva3.procesar()
    except Exception as e:
        logging.error(f"Error operación 4: {e}")
        operaciones.append(f"Error controlado: {e}")

    # 5. Confirmación de reserva
    try:
        cliente5 = Cliente("Marta", "marta@gmail.com", "3111111111")
        servicio4 = ReservaSala("Sala Básica", 20000)
        reserva4 = Reserva(cliente5, servicio4, 1)
        reserva4.confirmar()
        operaciones.append("Reserva confirmada correctamente")
        logging.info("Reserva confirmada")
    except Exception as e:
        logging.error(f"Error operación 5: {e}")
        operaciones.append(f"Error controlado: {e}")

    # 6. Cancelación de reserva
    try:
        cliente6 = Cliente("Pedro", "pedro@gmail.com", "3200000000")
        servicio5 = AlquilerEquipo("Proyector", 15000)
        reserva5 = Reserva(cliente6, servicio5, 2)
        reserva5.cancelar()
        operaciones.append("Reserva cancelada correctamente")
        logging.info("Reserva cancelada")
    except Exception as e:
        logging.error(f"Error operación 6: {e}")
        operaciones.append(f"Error controlado: {e}")

    # 7. Creación incorrecta de servicio
    try:
        servicio_invalido = ReservaSala("Sala Fantasma", -5000)
        operaciones.append("Servicio inválido creado")
    except Exception as e:
        logging.error(f"Error operación 7: {e}")
        operaciones.append(f"Error controlado: {e}")

    # 8. Cálculo con impuesto
    try:
        cliente7 = Cliente("Laura", "laura@gmail.com", "3009876543")
        servicio6 = AlquilerEquipo("Cámara", 25000)
        reserva6 = Reserva(cliente7, servicio6, 2)
        costo = servicio6.calcular_costo(impuesto=0.19)
        operaciones.append(f"Costo con IVA: ${costo}")
        logging.info("Costo calculado con impuesto")
    except Exception as e:
        logging.error(f"Error operación 8: {e}")
        operaciones.append(f"Error controlado: {e}")

    # 9. Cálculo con descuento
    try:
        cliente8 = Cliente("Andrés", "andres@gmail.com", "3012345678")
        servicio7 = Asesoria("Asesoría en Redes", 60000)
        reserva7 = Reserva(cliente8, servicio7, 1)
        costo = servicio7.calcular_costo(descuento=10000)
        operaciones.append(f"Costo con descuento: ${costo}")
        logging.info("Costo calculado con descuento")
    except Exception as e:
        logging.error(f"Error operación 9: {e}")
        operaciones.append(f"Error controlado: {e}")

    # 10. Error encadenado
    try:
        try:
            raise ValueError("Duración inválida")
        except ValueError as e:
            raise ReservaError("Error al procesar reserva") from e
    except Exception as chained:
        logging.error(f"Error operación 10: {chained}")
        operaciones.append(f"Error controlado con encadenamiento: {chained}")

    # Resultados finales
    print("\n===== RESULTADOS =====")
    for op in operaciones:
        print(op)
    print("\nEl sistema sigue funcionando correctamente.")

if __name__ == "__main__":
    ejecutar_pruebas()
