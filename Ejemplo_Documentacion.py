# Importar el modulo funciones matematicas para mostrar la documentacion
# CURSOS_ONLINE.PYTHON.Modulos  es la ruta donde esta el modulo
# from CURSOS_ONLINE.PYTHON.Modulos import Funciones_Matematicas
from Modulos import Funciones_Matematicas

class Areas:

	"""Esta clase calcula las areas de diferentes figuras geometricas"""

	def areaCuadrado(lado):

		"""Calcula el area de un cuadrado
		elevando al cuadrado el lado pasado por parametro"""

		return "El area del cuadrado es: " + str(lado*lado)

	def areaTriangulo(base, altura):

		"""Calcula el area de un triangulo utilizando los parametros base y altura"""

		return "El area del triangulo es: " + str((base*altura)/2)


# con help muestra en ejecucion la documentacion del objeto que queramos
help(Areas.areaCuadrado)

help(Areas)

help(Funciones_Matematicas)

