from tkinter import*
import random

#--------------------
#variables globales
#--------------------
BASE = 760
ALTURA = 220


#--------------------
#ventana principal
#--------------------
ventana_principal = Tk()
ventana_principal.title("graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("800x500")
ventana_principal.config(bg= "white")

#----------------------
#frame de graficacion
#----------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=780, height=240)
frame_graficacion.place(x=10, y=10)

#creacion canvas 
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

#---------------------
#frame de controles
#---------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=780, height=230)
frame_controles.place(x=10, y=260)

#---------------------
#frame de carretera
#---------------------
frame_carretera = Frame(frame_graficacion)
frame_carretera.config(bg="grey", width=630, height=30)
frame_carretera.place(x=100, y=80)

#---------------------
#frame de carretera
#---------------------
frame_linea_carretera = Frame(frame_graficacion)
frame_linea_carretera.config(bg="yellow", width=630, height=10)
frame_linea_carretera.place(x=100, y=90)

#---------------------
#frame de carretera
#---------------------
frame_carretera = Frame(frame_graficacion)
frame_carretera.config(bg="grey", width=630, height=30)
frame_carretera.place(x=100, y=150)

#---------------------
#frame de carretera
#---------------------
frame_linea_carretera = Frame(frame_graficacion)
frame_linea_carretera.config(bg="yellow", width=630, height=10)
frame_linea_carretera.place(x=100, y=160)

#agregar una imagen al canvas
img_carro1 = PhotoImage(file="img/carro1.png")
carro1 = c.create_image(BASE/20, ALTURA/2.6, image=img_carro1)

#agregar una imagen al canvas
img_carro2 = PhotoImage(file="img/carro2.png")
carro2 = c.create_image(BASE/20, ALTURA/1.4, image=img_carro2)

# texto para la salida 
texto_1 = c.create_text(BASE/10, ALTURA/4, anchor="center", text="S",font=("Arial", 10, "bold"),fill="yellow")
texto_2 = c.create_text(BASE/10, ALTURA/2.7, anchor="center", text="A",font=("Arial", 10, "bold"),fill="yellow")
texto_3 = c.create_text(BASE/10, ALTURA/2.1, anchor="center", text="L",font=("Arial", 10, "bold"),fill="yellow")
texto_4 = c.create_text(BASE/10, ALTURA/1.7, anchor="center", text="I",font=("Arial", 10, "bold"),fill="yellow")
texto_5 = c.create_text(BASE/10, ALTURA/1.4, anchor="center", text="D",font=("Arial", 10, "bold"),fill="yellow")
texto_6 = c.create_text(BASE/10, ALTURA/1.2, anchor="center", text="A",font=("Arial", 10, "bold"),fill="yellow")

# texto para la llegada
texto_1 = c.create_text(BASE-30, ALTURA/4, anchor="center", text="L",font=("Arial", 10, "bold"),fill="red1")
texto_2 = c.create_text(BASE-30, ALTURA/2.7, anchor="center", text="L",font=("Arial", 10, "bold"),fill="red1")
texto_3 = c.create_text(BASE-30, ALTURA/2.1, anchor="center", text="E",font=("Arial", 10, "bold"),fill="red1")
texto_4 = c.create_text(BASE-30, ALTURA/1.7, anchor="center", text="G",font=("Arial", 10, "bold"),fill="red1")
texto_5 = c.create_text(BASE-30, ALTURA/1.5, anchor="center", text="A",font=("Arial", 10, "bold"),fill="red1")
texto_6 = c.create_text(BASE-30, ALTURA/1.3, anchor="center", text="D",font=("Arial", 10, "bold"),fill="red1")
texto_7 = c.create_text(BASE-30, ALTURA-30, anchor="center", text="A",font=("Arial", 10, "bold"),fill="red1")

# boton para sumar
bt_convertir = Button(frame_graficacion,text="JUGAR")
bt_convertir.place(x=315, y=195, width=100, height=25)

#desplegar ventana
ventana_principal.mainloop()