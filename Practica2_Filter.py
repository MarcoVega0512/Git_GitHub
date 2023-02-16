# Se crea una clase para empleados
class Empleado:

	# Se crea un objeto con el constructor
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	# devuelve un string con la informacion de los datos del objeto Empleado
	def __str__(self):

		return "{} que trabaja como {} y tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
Empleado("Juan","Director",75000),
Empleado("Ana","Presidenta",85000),
Empleado("Antonio","Administrativo",25000),
Empleado("Sara","Secretaria",27000),
Empleado("Mario","Botones",21000)
]

# Filtra los empleados que cumplan la condicion del filter
salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salarios in salarios_altos:
	print(empleado_salarios)

