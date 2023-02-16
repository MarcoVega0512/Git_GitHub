class Vehiculos():

	# Crear un Constructor con las propiedades en comun - Estado Inicial
	def __init__(self,p_marca,p_modelo):
		self.marca=p_marca
		self.modelo=p_modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enmarcha,"\nAcelerando: ",
			self.acelera,"\nFrenando: ",self.frena)

class Furgoneta(Vehiculos):
	def carga(self,cargar):
		self.cargado=cargar

		if self.cargado==True:
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta No esta cargada"

class Moto(Vehiculos):
	hcaballito=""

	def caballito(self):
		self.hcaballito="Voy haciendo el Caballito"

	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enmarcha,"\nAcelerando: ",
			self.acelera,"\nFrenando: ",self.frena,"\n",self.hcaballito)

class VElectricos(Vehiculos):
	def __init__(self,p_marca,p_modelo):

		super().__init__(p_marca,p_modelo)

		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True

