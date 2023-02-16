#EJERCICIO DE CREACION DE UNA CALCULADORA

from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

# ---------------------------   CREACION DE VARIABLES GLOBALES ---------------------------------------------
operacion=""
resultado=0

# Crear una variable de tipo cadena de caracteres larga (Stringvar)
numeroPantalla=StringVar()

# --------------------------  CREACION DE FUNCIONES ---------------------------------------------------------

# Funcion para mostrar los numeros en objeto pantalla segun se presionan botones de numeros
def numeroPulsado(numeroTecla):
	global operacion

	if operacion!="":
		numeroPantalla.set(numeroTecla)
		operacion=""
	else:
		# numeroPantalla.get()  sireve para leer lo que hay en pantalla y lo concatena con el numero de parametro
		numeroPantalla.set(numeroPantalla.get() + numeroTecla)

# Funcion para limpiar objeto pantalla
def limpiaPantalla():
	global operacion
	global resultado
	
	numeroPantalla.set("")
	operacion=""
	resultado=0

# Funcion para eliminar el ultimo numero ingresado en objeto pantalla
def eliminaCaracterPantalla():
	pass

# Funcion para Sumar
def sumar(num):
	global operacion
	global resultado

	resultado+=float(num)

	operacion="suma"

	numeroPantalla.set(resultado)

# Funcion para Restar
def restar(num):
	global operacion
	global resultado

	resultado-=float(num)

	operacion="resta"

	numeroPantalla.set(resultado)

# Funcion para Sumar con tecla igual (=)
def igual():
	global resultado

	numeroPantalla.set(resultado+float(numeroPantalla.get()))

	resultado=0

# ----------------  DEFINICION DE PANTALLA DE RESULTADOS ----------------------
pantalla=Entry(miFrame, textvariable=numeroPantalla)
# columnspan=4 indica que objeto pantalla ocupara 4 columnas
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

# --------------- FILA 1 DE CALCULADORA ---------------------------------------
botonBorrar=Button(miFrame, text="<-", width=3, command=eliminaCaracterPantalla)
botonBorrar.grid(row=2,column=2, padx=1, pady=1)
botonBorrar=Button(miFrame, text="C", width=3, command=limpiaPantalla)
botonBorrar.grid(row=2,column=3, padx=1, pady=1)
botonDivide=Button(miFrame, text="/", width=3)
botonDivide.grid(row=2,column=4, padx=1, pady=1)

# --------------- FILA 2 DE CALCULADORA ---------------------------------------
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=3,column=1, padx=1, pady=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=3,column=2, padx=1, pady=1)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=3,column=3, padx=1, pady=1)
botonMultiplica=Button(miFrame, text="X", width=3)
botonMultiplica.grid(row=3,column=4, padx=1, pady=1)

# --------------- FILA 3 DE CALCULADORA ---------------------------------------
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=4,column=1, padx=1, pady=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=4,column=2, padx=1, pady=1)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=4,column=3, padx=1, pady=1)
botonResta=Button(miFrame, text="-", width=3, command=lambda:restar(numeroPantalla.get()))
botonResta.grid(row=4,column=4, padx=1, pady=1)

# --------------- FILA 4 DE CALCULADORA ---------------------------------------
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=5,column=1, padx=1, pady=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=5,column=2, padx=1, pady=1)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=5,column=3, padx=1, pady=1)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:sumar(numeroPantalla.get()))
botonSuma.grid(row=5,column=4, padx=1, pady=1)

# --------------- FILA 5 DE CALCULADORA ---------------------------------------
botonMasMenos=Button(miFrame, text="+/-", width=3)
botonMasMenos.grid(row=6,column=1, padx=1, pady=1)
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=6,column=2, padx=1, pady=1)
botonDecimal=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
botonDecimal.grid(row=6,column=3, padx=1, pady=1)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:igual())
botonIgual.grid(row=6,column=4, padx=1, pady=1)


raiz.mainloop()


