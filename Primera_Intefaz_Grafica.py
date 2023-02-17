# EJEMPLO DE COMO CREAR UNA INTERFAZ GRAFICA - PRIMEROS CONCEPTOS

# Se debe importar la biblioteca tkinter con todas sus clases/metodos/funciones
from tkinter import *

# Crear un objeto que se instancia con la clase Tk
raiz=Tk()

# Para poner un titulo en la ventana
raiz.title("Mi primera interfaz grafica - Rama Nueva")

# Para poder redimensionar una ventana utilizar el metodo resizable(par1,par2)
# donde par1 puede ser (0 o False) o (1 o True) - Par1 corresponde al ancho (width)
# donde par2 puede ser (0 o False) o (1 o True) - Par2 corresponde al alto (height)
raiz.resizable(True,True)

# Para cambiar el icono de barra en ventana - solo deben ser iconos (.ico)
raiz.iconbitmap("auto.ico")

# Cambiar tamaño de la ventana con metodo geometry ("Valor1xValor2")
# Valor1 corresponde al Ancho y Valor2 corresponde al Alto
# raiz.geometry("650x350")

# Con el metodo config() se pueden cambiar muchas caracteristicas de la ventana
raiz.config(bg="blue")   # bg para cambiar el color de fondo

# Crear un objeto que se instancia con la clase Frame()
miframe=Frame()

# Para dejar el frame dentro de la raiz se debe empaquetar usando metodo pack()
miframe.pack()    # Lo deja fijo en modo estandar

# Se debe configurar el tamaño del frame utilizando metodo config()
# El tamaño de la raiz se adecua al tamaño del frame
miframe.config(width="650", height="350")

# Para que frame se visualize cambiamos el color de fondo distinto al color de fonde de la raiz
miframe.config(bg="green")

# Para configurar un borde y un relieve en el frame
# para poder ver resultado el frame no debe poder redimensionar - miframe.pack()
miframe.config(bd=5)
miframe.config(relief="groove")

# Para cambiar el icono del cursor cuando se posiciona en el frame
miframe.config(cursor="hand2")

# Utilizando el metodo mainloop() se crea una ventana raiz  
# Debe ser la ultima instruccion despues de terminar de configurar la ventana
raiz.mainloop()

