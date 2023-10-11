#importar librerias de GUI
from tkinter import *
from tkinter import messagebox

#defino mi objeto ventana
window = Tk()
### area de ventana

#FUNCIONES
def MSG_INFO():
    messagebox.showinfo("caja de informacion", "informacion para el usuario")
def MSG_ERROR():
    messagebox.showerror("caja de ERROR", "informacion sobre el ERROR generado")

def MSG_WARNING():
    messagebox.showwarning("caja de Advertencia", "adevertir al usuario sobre algo")

def ASK_OKCANCEL():
    seleccion = messagebox.askokcancel("caja de 2 botones", "el usuario decide si OK o CANCELA")
    if seleccion == True:
        Etiqueta['text']="Usuario slecciono OK"
    else:
        Etiqueta['text']="Usuario dijo que CANCELAR"
        
def ASK_YESNO():
    seleccion = messagebox.askyesno("caja de Si o NO", "usuario SI o NO ?")
    if seleccion == False:
        Etiqueta['text']="Usuario dijo que NO"
    else:
        Etiqueta['text']="Usuario dijo que YESS"
def  ASK_QUESTION():
      messagebox.askquestion("caja de  botones, do you want sumit?")

def ASK_RETRYCANCEL():
    seleccion = messagebox.askretrycancel("Caja de volver y cancelar")
    if seleccion == False:
        Etiqueta['text']="Usuario dijo que cancelar"
    else:
        Etiqueta['text']="Usuario dijo que reintentar"
def ASK_YESNOCANCEL():
    seleccion = messagebox.askyesnocancel ("caja de 3 botones", "el usuario decide yes, no y cancel")
    if seleccion == True:
        Etiqueta['text']="Usuario dijo que YESS"
    elif seleccion == FALSE:
        Etiqueta['text']="Usuario dijo que NO"
    elif seleccion == None:
        Etiqueta ['text']="Usuario dijo CANCEL"
window.title("prueba de Cajas de mensajes")
#defino mis componentes
boton_ERROR = Button(window, text="caja de ERROR!", command=lambda:MSG_ERROR() )
boton_INFO = Button(window, text="caja de INFO", command=lambda:MSG_INFO() )
boton_WARNING = Button(window, text="caja de WARNING", command=lambda:MSG_WARNING() )
boton_OKCANCEL = Button(window, text="caja de OKCANCEL", command=lambda:ASK_OKCANCEL() )
boton_YESNO = Button(window, text="caja de SI o NO ", command=lambda:ASK_QUESTION()  )
boton_ASK_QUESTION = Button(window, text="Caja de pregunta ", command=lambda:ASK_YESNO()  )
boton_ASK_RETRYCANCEL = Button(window, text="Volver y cancelar ", command=lambda:ASK_RETRYCANCEL()  )
boton_ASK_YESNOCANCEL = Button(window, text="Volver y cancelar ", command=lambda:ASK_YESNOCANCEL()  )

Etiqueta = Label(window, text="resultado de opcion seleccionada por usario")
#genero layout de ventana
boton_ERROR.pack(padx=5, pady=3)
boton_INFO.pack(padx=5, pady=3)
boton_WARNING.pack(padx=5, pady=3)
boton_ASK_RETRYCANCEL.pack(padx=5, pady=3)
boton_OKCANCEL.pack(padx=5, pady=3)
boton_YESNO.pack(padx=5, pady=3)
boton_ASK_QUESTION.pack(padx=5, pady=3)
boton_ASK_YESNOCANCEL.pack(padx=5, pady=3)


Etiqueta.pack(padx=5, pady=3)
### termina area de ventana y todos sus objetos
window.mainloop()