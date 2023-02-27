# EJEMPLO DE COMO UTILIZAR ENTRY , TEXT, BUTTON EN UNA INTERFAZ GRAFICA
# CUADRO DE TEXTOS, CUADRO DE TEXTOS LARGOS Y BOTONES

# Se debe importar la biblioteca tkinter con todas sus clases/metodos/funciones
from tkinter import *

# Crear un objeto y se instancia con la clase Tk() - se crea la raiz de la interfaz
raiz=Tk()

# Para poner un titulo en la ventana
raiz.title("Empezando con GitHug - Prueba Pull Request")

# Crear un objeto y se instancia con la clase Frame() - se crea el frame dentro de la raiz
# y se define un tamaño del frame (ancho y alto)
miFrame=Frame(raiz, width=1200,height=600)

# Empaquetar el frame para que quede dentro de la raiz
miFrame.pack()

# Crear una variable de tipo cadena de caracteres
miNombre=StringVar()

# Crear un objeto y se instacia con la clase Label - indicar frame y el texto
nombreLabel=Label(miFrame, text="Nombre: ")

# Para mostrar se debe empaquetar el Label en el frame utilizando el metodo grid(row=0,column=0)
# row=0 indica que pondra el label en la primera fila de la grilla inmaginaria
# column=0 indica que pondra el label en la primera columna de la grilla inmaginaria
# sticky="w" indica que el texto lo justificara a la izquierda
# sticky="e" indica que el texto lo justificara a la derecha
# padx=2  indica que dara 2 pixeles de espacio a la izquierda y a la derecha
# pady=2  indica que dara 2 pixeles de espacio hacia arriba y hacia abajo
nombreLabel.grid(row=0,column=0, sticky="e", padx=2, pady=2)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1,column=0, sticky="e", padx=2, pady=2)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2,column=0, sticky="e", padx=2, pady=2)

passwordLabel=Label(miFrame, text="Password: ")
passwordLabel.grid(row=3,column=0, sticky="e", padx=2, pady=2)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4,column=0, sticky="e", padx=2, pady=2)

# Crear un objeto y se instacia con la clase Entry - indicar frame
# textvariable=miNombre  Esto indica que el objeto "CuadroNombre" esta asociado a la variable "miNombre"
cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0,column=1, padx=2, pady=2)
# fb="red"  cambiar el color del texto
# justify="right"  el ingreso del texto sera alineado a la derecha
cuadroNombre.config(fg="red", justify="right")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1, padx=2, pady=2)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2,column=1, padx=2, pady=2)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=3,column=1, padx=2, pady=2)
# show="*"  indica que reemplazara todos los caracteres por "*" para que no sea visible
cuadroPassword.config(show="*")

# Crear un objeto y se instacia con la clase Text - indicar el contenedor donde estara
# y se define un tamaño del recuadro de texto (ancho y alto)
textoComentario=Text(miFrame, width=16,height=5)
textoComentario.grid(row=4,column=1, padx=2, pady=2)

# Crear objeto y se instancia con la clase Scrollbar - indicar el contenedor padre (miFrame)
# command=textoComentario  indica que el scroll pertenece al objeto textoComentario
#.yview   indica que el scroll sera vertical (y)
scrollComentario=Scrollbar(miFrame, command=textoComentario.yview)
# Para que se vea el scroll se debe aplicar el metodo grid indicando la posicion en grilla inmaginaria
# sticky="nsew"  indica que el scroll tendra el mismo tamaño que el objeto textoComentario (altura)
scrollComentario.grid(row=4,column=2, sticky="nsew")
# Para que el indicador del scroll se mueva en la posicion del Text se debe configurar el metodo
# yscrollcommand que lleva el nombre del scroll (scrollComentario.set)
textoComentario.config(yscrollcommand=scrollComentario.set)

# Agregar codigo de acciones dentro del boton
def codigoBotonMostrar():
	miNombre.set("Marco")   # a la variable se le esta asignando un texto

# Crear un objeto y se instacia con la clase Button - indicar el contenedor donde estara
# command=codigoBotonMostrar   Esto hace que se llamara a la funcion para realizar acciones, cuando se presione el boton
botonMostrar=Button(miFrame, text="Mostrar Nombre", command=codigoBotonMostrar)
botonMostrar.grid(row=10,column=4, padx=10, pady=10)

botonSalir=Button(raiz, text="Salir")
botonSalir.pack(side=LEFT, padx=10, pady=10)

# DEBE SER LA ULTIMA INSTRUCCION
raiz.mainloop()

