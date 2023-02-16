def numero_par(num):

	if num % 2==0:

		return True

numeros=[17,24,7,39,8,51,92]	

# filter tiene 2 parametros, funcion a llamar y lista de numeros	
# el metodo "list" lo que hace es devolver el objeto en formato de lista
print(list(filter(numero_par,numeros)))

# Utilizando funciones LAMBDA
print ("\nRESULTADO UTILIZANDO FUNCIONES LAMBDA")

print(list(filter(lambda numero_Par: numero_Par%2==0,numeros)))


