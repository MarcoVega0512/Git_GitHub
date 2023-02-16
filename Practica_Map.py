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
Empleado("Juan","Director",6700),
Empleado("Ana","Presidenta",7500),
Empleado("Antonio","Administrativo",2100),
Empleado("Sara","Secretaria",2150),
Empleado("Mario","Botones",1800)
]

def calculo_comision(empleado):

	if empleado.salario<=3000:

		empleado.salario=empleado.salario*1.03

	return empleado

listaEmpleadosComision=map(calculo_comision,listaEmpleados)

for empleado in listaEmpleadosComision:

	print(empleado)

