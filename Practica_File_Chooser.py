#EJEMPLO DE COMO REALIZAR VENTANAS ABRIR Y GUARDAR ARCHIVOS - INTERFAZ GRAFICA

from tkinter import *
from tkinter import messagebox  # importar biblioteca para utilizar ventanas emergentes
from tkinter import filedialog  # importar biblioteca para utilizar ventanas emergentes abrir/guardar archivos y directorios

raiz=Tk()
raiz.title("Ejemplo Ventanas Abrir/Guardar Archivos y Directorios")
raiz.geometry("500x200")

def abrirArchivo():
	# El metodo askopenfilename abre una ventana de windows para buscar el archivo que se quiere abrir
	# este metodo devuelve la ruta y nombre de archivo seleccionado para abrir
	# con este parametro initialdir="c:" se indica desde donde comenzara la busqueda del archivo
	# con el parametro filetypes se puede indicar los tipos de archivos a mostrar ventana de busqueda
	archivo=filedialog.askopenfilename(title="Abrir", initialdir="C:/", filetypes=(("Archivos de Excel","*.xlsx"),
		("Archivos de texto","*.txt"),("Todos los Archivos","*.*")))

	print("La ruta donde se encuentra el archivo es: ",archivo)

def guardarArchivo():
	nuevoArchivo=filedialog.asksaveasfilename(title="Guardar archivo...",defaultextension=".txt",
		filetypes=(("Archivo de texto","*.txt"),))

Button(raiz, text="Abrir archivo", command=abrirArchivo).pack()
Button(raiz, text="Guardar archivo", command=guardarArchivo).pack()


raiz.mainloop()


