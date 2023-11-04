import serial
import time
import tkinter as tk

GERA = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

def write_read(x):
    GERA.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = GERA.readline()
    return data

def send_data():
    num = entry.get()
    value = write_read(num)
    result_label.config(text=value)

# Crear la ventana principal
root = tk.Tk()
root.title("Control de PACO")

# Crear una etiqueta
label = tk.Label(root, text="Ingrese un número:")
label.pack()

# Crear una casilla de entrada
entry = tk.Entry(root)
entry.pack()

# Crear un botón para enviar el valor
send_button = tk.Button(root, text="Enviar", command=send_data)
send_button.pack()

# Crear una etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
result_label.pack()

# Bucle principal de la aplicación
root.mainloop()

# Cerrar la conexión serial al salir
GERA.close()
