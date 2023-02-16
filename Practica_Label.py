# EJEMPLO DE COMO UTILIZAR LABEL EN UNA INTERFAZ GRAFICA

# Se debe importar la biblioteca tkinter con todas sus clases/metodos/funciones
from tkinter import *

# Crear un objeto y se instancia con la clase Tk() - se crea la raiz de la interfaz
root=Tk()

# Crear un objeto y se instancia con la clase Frame() - se crea el frame dentro de la raiz
miFrame=Frame(root, width=500,height=400)

# Empaquetar el frame para que quede dentro de la raiz
miFrame.pack()

# Crear un objeto y se instacia con la clase Label - indicar frame y el texto
# con la propiedad fg="red" se cambia el color de la fuente
# con la propiedad font=("Magneto",18) se cambia el el tipo de letra y el tamaño de la letra
# con la propiedad bd=1 indica el grosor del borde del label
# con la propiedad relief="solid" le da relieve al borde del label
miLabel=Label(miFrame, text="Hola alumnos de Pyhton",fg="red", font=("Magneto",18),bd=1, relief="solid")

# Para mostrar se debe empaquetar el Label en el frame utilizando el metodo place(x=val1, y=val2)
# donde val1 es la cantidad de pixel que habra desde borde izquierdo para escribir el label
# donde val2 es la cantidad de pixel que habra desde borde superior para escribir el label
miLabel.place(x=10,y=10)

# Crear un objeto y se instacia con la clase PhotoImage - indicar la ruta y nombre de la imagen
miImagen=PhotoImage(file="mouse.png")

# Label con una imagen
# Crear un objeto y se instacia con la clase Label - indicar frame y la imagen
# con la propiedad bd=1 indica el grosor del borde del label
# con la propiedad relief="solid" le da relieve al borde del label
miLabel=Label(miFrame, image=miImagen,bd=1, relief="solid")
miLabel.place(x=10,y=50)

# este metodo debe ir al final del programa
root.mainloop()

