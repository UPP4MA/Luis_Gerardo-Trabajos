import tkinter as tk
from tkinter import messagebox

# Funciones para los comandos de la barra de menú
def new_file():
    messagebox.showinfo("File", "New File selected")

def open_file():
    messagebox.showinfo("File", "Open selected")

def save_file():
    messagebox.showinfo("File", "Save selected")

def cut_text():
    messagebox.showinfo("Edit", "Cut selected")

def copy_text():
    messagebox.showinfo("Edit", "Copy selected")

def paste_text():
    messagebox.showinfo("Edit", "Paste selected")

def select_all():
    messagebox.showinfo("Edit", "Select All selected")

def tk_help():
    messagebox.showinfo("Help", "Tk Help selected")

def demo():
    messagebox.showinfo("Help", "Demo selected")
    
def salir():
    ventana.quit()
    
# Crear la ventana
ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title('MenuBAR')

# Crear una barra de menú
menubar = tk.Menu(ventana)

# Menú File
file = tk.Menu(menubar, tearoff=1)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=new_file)
file.add_command(label='Open...', command=open_file)
file.add_command(label='Save', command=save_file)

# Menú Edit
edit = tk.Menu(menubar, tearoff=1)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=cut_text)
edit.add_command(label='Copy', command=copy_text)
edit.add_command(label='Paste', command=paste_text)
edit.add_command(label='Select All', command=select_all)

# Menú Help
help_ = tk.Menu(menubar, tearoff=1)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=tk_help)
help_.add_command(label='Demo', command=demo)
help_.add_command(label='Salir', command=salir)

# Configurar la barra de menú en la ventana
ventana.config(menu=menubar)

# Ejecutar la aplicación
ventana.mainloop()