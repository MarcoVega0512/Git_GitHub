def areaTriangulo(base, altura):

	"""
	Calcula el area de un triangulo utilizando los parametros base y altura

	>>> areaTriangulo(3,6)
	'El area del triangulo es: 9.0'

	>>> areaTriangulo(4,5)
	'El area del triangulo es: 11.0'

	>>> areaTriangulo(9,3)
	'El area del triangulo es: 13.5'

	"""

	return "El area del triangulo es: " + str((base*altura)/2)

import doctest
doctest.testmod()

