#EJEMPLO DE COMO UTILIZAR LOS CHECKBUTTON - INTERFAZ GRAFICA

from tkinter import *

raiz=Tk()

raiz.title("Ejemplo Uso de CheckButton")

miFrame=Frame(raiz, width=600,height=100)
miFrame.pack()

varPlaya=IntVar()
varMontana=IntVar()
varTurismoRural=IntVar()

def opcionesViaje():
	opcionEscogida=""

	if varPlaya.get()==1:
		opcionEscogida+=" Playa"

	if varMontana.get()==1:
		opcionEscogida+=" Montaña"

	if varTurismoRural.get()==1:
		opcionEscogida+=" Turismo Rural"

	etiquetaViaje.config(text="viajaras a la"+opcionEscogida)


foto=PhotoImage(file="avion1.png")
imagenLabel=Label(miFrame,image=foto)
imagenLabel.grid(row=1,column=1, padx=10, pady=10)

destinoLabel=Label(miFrame,text="Elige Destinos")
destinoLabel.grid(row=2,column=1, padx=1, pady=1)

# variable=varPlaya  Asocia el Checkbutton a una variable para obtener valor cuando esta seleccionada o sin seleccionar
# onvalue=1    Valor que tendra la opcion del CheckButton cuando este seleccionada
# offvalue=0   Valor que tendra la opcion del CheckButton cuando NO este seleccionada
# command=opcionesViaje  Con esto llama a la funcion
opcionPlaya=Checkbutton(miFrame,text="Playa",variable=varPlaya,onvalue=1,offvalue=0,command=opcionesViaje)
opcionPlaya.grid(row=3,column=1, padx=1, pady=1)

opcionMontana=Checkbutton(miFrame,text="Montaña",variable=varMontana,onvalue=1,offvalue=0,command=opcionesViaje)
opcionMontana.grid(row=4,column=1, padx=1, pady=1)

opcionTurismoRural=Checkbutton(miFrame,text="Turismo Rural",variable=varTurismoRural,onvalue=1,offvalue=0,command=opcionesViaje)
opcionTurismoRural.grid(row=5,column=1, padx=1, pady=1)

etiquetaViaje=Label(miFrame)
etiquetaViaje.grid(row=6,column=1, padx=1, pady=1)

raiz.mainloop()


