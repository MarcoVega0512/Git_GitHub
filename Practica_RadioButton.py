#EJEMPLO DE COMO UTILIZAR LOS RADIOBUTTON - INTERFAZ GRAFICA

from tkinter import *

raiz=Tk()

raiz.title("Ejemplo Uso de Radiobutton")

miFrame=Frame(raiz)
miFrame.pack()

# Variables para agrupar mas de un RavioButton  como uno solo
varOpcionGenero=IntVar()
varOpcionEstudios=IntVar()

def imprimir(tipoRadioButton):

	# varOpcionGenero.get()   Para obtener el valor que tiene la opcion del RadioButton
	if tipoRadioButton=="Genero":
		if varOpcionGenero.get()==1:
			etiquetaGenero.config(text="Has elegido Masculino")
		elif varOpcionGenero.get()==2:
			etiquetaGenero.config(text="Has elegido Femenino")
		else:
			etiquetaGenero.config(text="Has elegido Otro")
	elif tipoRadioButton=="Estudio":
		if varOpcionEstudios.get()==1:
			etiquetaEstudio.config(text="Has elegido Basica")
		elif varOpcionEstudios.get()==2:
			etiquetaEstudio.config(text="Has elegido Media")
		else:
			etiquetaEstudio.config(text="Has elegido Superior")

generoLabel=Label(miFrame,text="Seleccione el Genero: ")
generoLabel.grid(row=1,column=1, padx=10, pady=10)

# variable=varOpcionGenero  Indica a que grupo de opciones pertenece
# value=1    Valor que tendra la opcion del RadioButton
opcionMsuclino=Radiobutton(miFrame,text="Masculino",variable=varOpcionGenero,value=1,command=lambda:imprimir("Genero"))
opcionMsuclino.grid(row=2,column=1, padx=1, pady=1)

opcionFemenino=Radiobutton(miFrame,text="Femenino",variable=varOpcionGenero,value=2,command=lambda:imprimir("Genero"))
opcionFemenino.grid(row=3,column=1, padx=1, pady=1)

opcionOtros=Radiobutton(miFrame,text="Otro",variable=varOpcionGenero,value=3,command=lambda:imprimir("Genero"))
opcionOtros.grid(row=4,column=1, padx=1, pady=1)

estudioLabel=Label(miFrame,text="Seleccione Nivel de Estudio: ")
estudioLabel.grid(row=1,column=3, padx=10, pady=10)

opcionBasica=Radiobutton(miFrame,text="Basica",variable=varOpcionEstudios,value=1,command=lambda:imprimir("Estudio"))
opcionBasica.grid(row=2,column=3, padx=1, pady=1)

opcionMedia=Radiobutton(miFrame,text="Media",variable=varOpcionEstudios,value=2,command=lambda:imprimir("Estudio"))
opcionMedia.grid(row=3,column=3, padx=1, pady=1)

opcionSuperior=Radiobutton(miFrame,text="Superior",variable=varOpcionEstudios,value=3,command=lambda:imprimir("Estudio"))
opcionSuperior.grid(row=4,column=3, padx=1, pady=1)


etiquetaGenero=Label(miFrame)
etiquetaGenero.grid(row=6,column=1, padx=1, pady=1)

etiquetaEstudio=Label(miFrame)
etiquetaEstudio.grid(row=6,column=3, padx=1, pady=1)


raiz.mainloop()


