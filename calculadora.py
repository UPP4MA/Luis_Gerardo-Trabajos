from tkinter import *

ventana = Tk()
ventana.title("calculadora basica")

i = 0

#entrada
e_texto = Entry(ventana, font = ("Arial 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady=5)

#Funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
    
def borrar():
    e_texto.delete(0, END)
    i = 0
    
def back ():
    global i
    i -= 1
    e_texto.delete(i,END)
    
def hacer_operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0,resultado)
    i = 0   
    
def switchButtonState():
    if (boton_ON["text"] == "ON"):
        boton_ON ["text"] = "OFF"
    else:
        boton_ON["text"] = "ON"
        
    if (boton1["state"] == NORMAL):
        boton1 ["state"] = DISABLED 
    else:
        boton1 ["state"] = NORMAL  
        
    if (boton2["state"] == NORMAL):
        boton2 ["state"] = DISABLED 
    else:
        boton2 ["state"] = NORMAL
        
    if (boton3["state"] == NORMAL):
        boton3 ["state"] = DISABLED 
    else:
        boton3 ["state"] = NORMAL
        
    if (boton4["state"] == NORMAL):
        boton4 ["state"] = DISABLED 
    else:
        boton4 ["state"] = NORMAL  
        
    if (boton5["state"] == NORMAL):
        boton5 ["state"] = DISABLED 
    else:
        boton5 ["state"] = NORMAL  
        
    if (boton6["state"] == NORMAL):
        boton6 ["state"] = DISABLED 
    else:
        boton6 ["state"] = NORMAL  
        
    if (boton7["state"] == NORMAL):
        boton7 ["state"] = DISABLED 
    else:
        boton7 ["state"] = NORMAL  
        
    if (boton8["state"] == NORMAL):
        boton8 ["state"] = DISABLED 
    else:
        boton8 ["state"] = NORMAL  
        
    if (boton9["state"] == NORMAL):
        boton9 ["state"] = DISABLED 
    else:
        boton9 ["state"] = NORMAL  
        
    if (boton0["state"] == NORMAL):
        boton0 ["state"] = DISABLED 
    else:
        boton0 ["state"] = NORMAL  
        
    if (boton_borrar["state"] == NORMAL):
        boton_borrar ["state"] = DISABLED 
    else:
        boton_borrar ["state"] = NORMAL
        
    if (boton_parentesis1["state"] == NORMAL):
        boton_parentesis1 ["state"] = DISABLED 
    else:
        boton_parentesis1 ["state"] = NORMAL
        
    if (boton_parentesis2["state"] == NORMAL):
        boton_parentesis2 ["state"] = DISABLED 
    else:
        boton_parentesis2 ["state"] = NORMAL
        
    if (boton_punto["state"] == NORMAL):
        boton_punto ["state"] = DISABLED 
    else:
        boton_punto ["state"] = NORMAL
        
    if (boton_back["state"] == NORMAL):
        boton_back ["state"] = DISABLED 
    else:
        boton_back ["state"] = NORMAL  
        
    if (boton_div["state"] == NORMAL):
        boton_div ["state"] = DISABLED 
    else:
        boton_div ["state"] = NORMAL 
        
    if (boton_mult["state"] == NORMAL):
        boton_mult ["state"] = DISABLED 
    else:
        boton_mult ["state"] = NORMAL 
        
    if (boton_sum["state"] == NORMAL):
        boton_sum ["state"] = DISABLED 
    else:
        boton_sum ["state"] = NORMAL 
        
    if (boton_rest["state"] == NORMAL):
        boton_rest ["state"] = DISABLED 
    else:
        boton_rest ["state"] = NORMAL 
        
    if (boton_igual["state"] == NORMAL):
        boton_igual ["state"] = DISABLED 
    else:
        boton_igual ["state"] = NORMAL       
            
#Botones
boton_ON = Button(ventana, background= "purple", foreground= "yellow", text= "ON", width= 8, height=4, command=lambda:switchButtonState() )

boton1 = Button(ventana, foreground= "blue", text = "1", width = 6, height = 3,state=DISABLED,command = lambda: click_boton(1))
boton2 = Button(ventana, foreground= "blue",text = "2", width = 6, height = 3,state=DISABLED, command = lambda: click_boton(2))
boton3 = Button(ventana, foreground= "blue",text = "3", width = 6, height = 3,state=DISABLED, command = lambda: click_boton(3))
boton4 = Button(ventana, foreground= "blue",text = "4", width = 6, height = 3,state=DISABLED, command = lambda: click_boton(4))
boton5 = Button(ventana, foreground= "blue",text = "5", width = 6, height = 3,state=DISABLED, command = lambda: click_boton(5))
boton6 = Button(ventana, foreground= "blue",text = "6", width = 6, height = 3,state=DISABLED, command = lambda: click_boton(6))
boton7 = Button(ventana, foreground= "blue",text = "7", width = 6, height = 3,state=DISABLED, command = lambda: click_boton(7))
boton8 = Button(ventana, foreground= "blue",text = "8", width = 6, height = 3,state=DISABLED, command = lambda: click_boton(8))
boton9 = Button(ventana, foreground= "blue",text = "9", width = 6, height = 3,state=DISABLED, command = lambda: click_boton(9))
boton0 = Button(ventana, foreground= "blue",text = "0", width = 18, height = 3,state=DISABLED, command = lambda: click_boton(0))

boton_borrar = Button(ventana, font= "calibri", text = "AC", width = 5, height = 3,state=DISABLED, command = lambda: borrar())
boton_parentesis1 = Button(ventana, font= "calibri", text = "(", width = 5, height = 3,state=DISABLED,command = lambda: click_boton("("))
boton_parentesis2 = Button(ventana, font= "calibri", text = ")", width = 5, height = 3,state=DISABLED, command = lambda: click_boton(")"))
boton_punto = Button(ventana,font= "calibri", text = ".", width = 5, height = 3,state=DISABLED,command = lambda: click_boton("."))
boton_back = Button(ventana,font= "calibri", text = "<-", width = 5, height = 3,state=DISABLED,command = lambda: back())

boton_div = Button(ventana, borderwidth= "7", text = "/", width = 5, height = 3,state=DISABLED,command = lambda: click_boton("/"))
boton_mult = Button(ventana, borderwidth= "7", text = "x", width = 5, height = 3,state=DISABLED,command = lambda: click_boton("*"))
boton_sum = Button(ventana, borderwidth= "7", text = "+", width = 5, height = 3,state=DISABLED,command = lambda: click_boton("+"))
boton_rest = Button(ventana, borderwidth= "7", text = "-", width = 5, height = 3,state=DISABLED,command = lambda: click_boton("-"))
boton_igual = Button(ventana, borderwidth= "7", text = "=", width = 5, height = 3,state=DISABLED,command = lambda: hacer_operacion())

#agregar  botones en pantalla
boton_borrar.grid(row = 1, column= 0, padx= 5, pady = 5)
boton_parentesis1.grid(row = 1, column= 1, padx= 5, pady = 5)
boton_parentesis2.grid(row = 1, column= 2, padx= 5, pady = 5)
boton_div.grid(row = 1, column= 3, padx= 5, pady = 5)

boton7.grid(row = 2, column= 0, padx= 5, pady = 5)
boton8.grid(row = 2, column= 1, padx= 5, pady = 5)
boton9.grid(row = 2, column= 2, padx= 5, pady = 5)
boton_mult.grid(row = 2, column= 3, padx= 5, pady = 5)

boton4.grid(row = 3, column= 0, padx= 5, pady = 5)
boton5.grid(row = 3, column= 1, padx= 5, pady = 5)
boton6.grid(row = 3, column= 2, padx= 5, pady = 5)
boton_sum.grid(row = 3, column= 3, padx= 5, pady = 5)

boton1.grid(row = 4, column= 0, padx= 5, pady = 5)
boton2.grid(row = 4, column= 1, padx= 5, pady = 5)
boton3.grid(row = 4, column= 2, padx= 5, pady = 5)
boton_rest.grid(row = 4, column= 3, padx= 5, pady = 5)

boton0.grid(row = 5, column= 0,columnspan = 2, padx= 5, pady = 5)
boton_punto.grid(row = 5, column= 2, padx= 5, pady = 5)
boton_igual.grid(row = 5, column= 3, padx= 5, pady = 5)

boton_back.grid(row = 6 , column= 0, padx= 5, pady = 5)
boton_ON.grid(row = 6 , column= 1, padx= 5, pady = 5)
ventana.mainloop()