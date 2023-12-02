import tkinter as tk
from tkinter import ttk, messagebox
import socket
import threading

class ArduinoGUI:
    def _init_(self, root):
        self.root = root
        self.root.title("Control de Arduino")

        # Variables
        self.speed_var = tk.DoubleVar()
        self.speed_var.set(0)

        # Crear elementos de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Barra de velocidad para controlar la velocidad de los motores
        speed_label = ttk.Label(self.root, text="Velocidad de los motores:")
        speed_scale = ttk.Scale(self.root, from_=0, to=255, variable=self.speed_var, orient="horizontal", command=self.send_speed)
        speed_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        speed_scale.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Etiqueta para mostrar mensajes del sensor
        self.sensor_message_label = ttk.Label(self.root, text="")
        self.sensor_message_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botón de conexión
        connect_button = ttk.Button(self.root, text="Conectar al Servidor", command=self.connect_to_server)
        connect_button.grid(row=2, column=0, columnspan=2, pady=10)

    def send_speed(self, value):
        # Enviar la velocidad al servidor cuando la barra se ajusta
        try:
            speed = int(value)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect(("ip_del_servidor", 5555))
                client_socket.send(f"S{speed}".encode())
        except ValueError:
            pass

    def connect_to_server(self):
        try:
            # Conectar al servidor
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.connect(("ip_del_servidor", 5555))
            # Iniciar hilo para escuchar mensajes del servidor
            threading.Thread(target=self.receive_messages).start()
            messagebox.showinfo("Conexión Exitosa", "Conexión establecida correctamente con el servidor.")
        except Exception as e:
            # Manejar errores de conexión
            messagebox.showerror("Error de Conexión", f"No se pudo conectar al servidor: {e}")

    def receive_messages(self):
        while True:
            try:
                message = self.server_socket.recv(1024).decode()
                if message.startswith("DETECTADO"):
                    self.sensor_message_label.config(text="¡Sensor detectó algo!")
                elif message.startswith("NO_DETECCION"):
                    self.sensor_message_label.config(text="No se detecta nada.")
            except Exception as e:
                # Manejar errores de recepción
                print(f"Error de recepción: {e}")
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoGUI(root)
    root.mainloop()