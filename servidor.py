import socket
import threading
import serial
import time

# Configuración del puerto serie (para la comunicación con Arduino)
ser = serial.Serial('COM4', 9600)  # Reemplaza 'COM4' con el puerto correcto
time.sleep(2)  # Esperar a que se establezca la conexión

# Configuración del servidor
host = '192.168.65.171'  # Puedes cambiarlo según tu configuración de red
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print(f"Servidor escuchando en {host}:{port}")

def handle_client(client_socket):
    try:
        while True:
            # Leer la distancia desde el Arduino
            distance_str = ser.readline().decode().strip()
            print(f"Distancia recibida desde Arduino: {distance_str}")

            # Enviar la distancia al cliente
            client_socket.send(distance_str.encode())

            # Recibir velocidad desde el cliente y controlar los motores
            distance_str = client_socket.recv(1023).decode()
            if distance_str.isdigit():
                velocidad = int(distance_str)
                ser.write(str(velocidad).encode())
                print(f"Velocidad de los motores actualizada: {velocidad}")
            else:
                print("Datos no válidos para la velocidad.")

            time.sleep(1)  # Esperar antes de la siguiente lectura
    except (socket.error, serial.SerialException, ConnectionResetError):
        print('Error en la conexión o en la lectura del sensor.')

    finally:
        print("Cerrando la conexión con el cliente.")
        client_socket.close()

while True:
    try:
        client, addr = server.accept()
        print(f"Conexión establecida desde {addr}")

        # Iniciar un hilo para manejar la comunicación con el cliente
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
    except socket.error as e:
        print(f'Error al aceptar la conexión: {e}')

# Cerrar el socket del servidor cuando termine
server.close()
