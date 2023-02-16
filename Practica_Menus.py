#EJEMPLO DE COMO REALIZAR UN MENU - INTERFAZ GRAFICA

from tkinter import *
from tkinter import messagebox  # importar biblioteca para utilizar ventanas emergentes

raiz=Tk()
raiz.title("Ejemplo Creacion de Menus")

# Crear una funcion la que generara las ventanas emergentes
def informacionAdicional():
	# El metodo showinfo solo muestra informacion y tiene 2 parametros
	# Primer parametro es el texto que aparece como titulo (cabecera)
	# Segundo parametro es el texto que aparecera como detalle (cuerpo)
	messagebox.showinfo("Menu de Ejemplo","Este es una aplicacion de ejemplo de como se crea un Menú")

def avisoLicencia():
	# El metodo showwarning emite un mensaje de alerta y tiene 2 parametros
	# Primer parametro es el texto que aparece como titulo (cabecera)
	# Segundo parametro es el texto que aparecera como detalle (cuerpo)
	messagebox.showwarning("Licencia","Producto bajo licencia de Marco Vega")

def salirAplicacion():
	# El metodo askquestion emite un mensaje de pregunta con 2 opciones posibles - tiene 2 parametros
	# Primer parametro es el texto que aparece como titulo (cabecera)
	# Segundo parametro es el texto que aparecera como detalle (cuerpo)
	# Este metodo devuelve un valor dependiendo de la opcion seleccionada
#	respuestaSalir=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")

#	if respuestaSalir=="yes":
#		raiz.destroy()   # Este metodo destroy() hace que se salga de la aplicacion

	# Este Metodo askokcancel es similar a askquestion solo cambia la descripcion en botones y el valor de devuelve
	respuestaSalir=messagebox.askokcancel("Salir","¿Deseas salir de la aplicación?")

	if respuestaSalir==True:
		raiz.destroy()   # Este metodo destroy() hace que se salga de la aplicacion

def cerrarDocumento():
	# El metodo askretrycancel emite un mensaje de pregunta con 2 opciones posibles - tiene 2 parametros
	respuestaCerrar=messagebox.askretrycancel("Reintentar","No es posible cerrar. Documento bloqueado")

	if respuestaCerrar==False:
		raiz.destroy()   # Este metodo destroy() hace que se salga de la aplicacion

def guardarDocumento():
	messagebox.showerror("Guardar","No hay documento a guardar")

# Crar un objeto e instanciarlo a la clase Menu (Defincion del Menu)
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=400, height=300)

# Se define el elemento del menu y se instancia con la clase Menu y que pertenece al objeto barraMenu
# tearoff=0   Elimina Fila que pone automaticamente cuando el menu esta vacio
menuArchivo=Menu(barraMenu, tearoff=0)
# Se define el nombre que tendra el elemento del menu
barraMenu.add_cascade(label="Archivo",menu=menuArchivo)
# Para agregar las opcion del Menu "Archivo" (Submenus)
menuArchivo.add_command(label="Nuevo")
menuArchivo.add_command(label="Guardar",command=guardarDocumento)
menuArchivo.add_command(label="Guarcad Como")
# el metodo add_separator() coloca una barra continua para separar las opciones
menuArchivo.add_separator()
menuArchivo.add_command(label="Cerrar",command=cerrarDocumento)
menuArchivo.add_command(label="Salir",command=salirAplicacion)

menuEdicion=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Edicion",menu=menuEdicion)
menuEdicion.add_command(label="Copiar")
menuEdicion.add_command(label="Cortar")
menuEdicion.add_command(label="Pegar")

menuHerramientas=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Herramientas",menu=menuHerramientas)

menuAyuda=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)
menuAyuda.add_command(label="Licencia",command=avisoLicencia)
# command=informacionAdicional   Llama a la funcion que levanta la ventana emergente
menuAyuda.add_command(label="Acerca de..",command=informacionAdicional)


raiz.mainloop()


