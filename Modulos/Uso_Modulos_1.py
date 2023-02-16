# EJEMPLO DE MODULOS PROPIOS

# Para utilizar un modulo se debe importar - El Modulo debe estar en la misma carpeta 
import Funciones_Matematicas

print ("PRIMERA FORMA - UTILIZANDO IMPORT DEL MODULO")
# Para utilizar una funcion del modulo se debe poner nombre modulos punto nombre funcion
Funciones_Matematicas.sumar(5,15)

Funciones_Matematicas.restar(35,10)

Funciones_Matematicas.multiplicar(8,12)

print ("\n\nSEGUNDA FORMA - UTILIZANDO FORM MODULO IMPORT FUNCION")

# Con esto se declara la funcion a utilizar del modulo para no poner nombre modulos punto nombre funcion
from Funciones_Matematicas import sumar  # Se debe hacer por cada funcion a utilizar
sumar(5,15)

from Funciones_Matematicas import restar
restar(35,10)

from Funciones_Matematicas import multiplicar
multiplicar(8,12)

print ("\n\nTERCERA FORMA - UTILIZANDO FORM MODULO IMPORT *")

# Con esto se declara que todas las funciones del modulo quedan disponibles para utilizar
from Funciones_Matematicas import *  # Ocupa mas recursos de memoria

sumar(5,15)
restar(35,10)
multiplicar(8,12)


