# importar un modulo
from tkinter import *
  
# creando una ventana
ventana = Tk()
  
# geometria de la ventana
ventana.geometry("400x400")
  
# Add title
ventana.title('Menu Demonstration')
  
# creando menuBAR
menubar = Menu(ventana)
  
# Añadiendo filas, menus y submenus
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File')
file.add_command(label='Open...')
file.add_command(label='Save')
  
# añadiendo Edit Menu y SubMenus
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut')
edit.add_command(label='Copy')
edit.add_command(label='Paste')
edit.add_command(label='Select All')
  
# Añadiendo Help Menu y SubMenus
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help')
help_.add_command(label='Demo')
  
# display Menu
ventana.config(menu=menubar)
  
# Ejecutar Tkinter
ventana.mainloop()