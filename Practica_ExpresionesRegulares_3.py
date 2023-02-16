# EJEMPLOS DE EXPRESIONES REGULARES USANDO RANGOS
import re 

lista_nombres=['Ana',
				'Pedro',
				'María',
				'Rosa',
				'Sandra',
				'Celia']

print("Elementos que contengan un rango de caracteres en el texto")				

for elemento in lista_nombres:

	# con "[o-t]" (rango) se indica que busque todos los elementos que contenga un caracteres entre la "o" y la "t"
	if re.findall('[o-t]',elemento): 

		print(elemento)

print("\nElementos que comiencen con un rango de caracteres en el texto")				

for elemento in lista_nombres:

	# con "^[O-T]" (rango) se indica que busque todos los elementos que comiencen con un caracteres entre la "O" y la "T"
	if re.findall('^[O-T]',elemento): 

		print(elemento)

print("\nElementos que terminen con un rango de caracteres en el texto")				

for elemento in lista_nombres:

	# con "[o-t]$" (rango) se indica que busque todos los elementos que terminen con un caracteres entre la "o" y la "t"
	if re.findall('[o-t]$',elemento): 

		print(elemento)

lista_nombres2=['Ma1',
				'Se1',
				'Ma2',
				'Bar1',
				'Ma3',
				'Va1',
				'Va2',
				'Ma4',
				'MaA',
				'Ma5',
				'MaB',
				'MaC']

print("\nElementos que contengan un rango de numeros en el texto")				

for elemento in lista_nombres2:

	# con "Ma[0-3]" (rango) se indica que busque todos los elementos que contenga "Ma" y un rango entre "0" y "3"
	if re.findall('Ma[0-3]',elemento): 

		print(elemento)

print("\nElementos que no esten en un rango de numeros en el texto")				

for elemento in lista_nombres2:

	# con "Ma[^0-3]" (rango) se indica que busque todos los elementos que contenga "Ma" y no esten en el rango entre "0" y "3"
	if re.findall('Ma[^0-3]',elemento): 

		print(elemento)

print("\nElementos que contengan un rango de numeros o un rango de caracteres en el texto")				

for elemento in lista_nombres2:

	# con "Ma[0-3A-B]" (rango) se indica que busque todos los elementos que contenga "Ma" y un rango entre "0" y "3"
	# o con un rango entre "A" y "B"
	if re.findall('Ma[0-3A-B]',elemento): 

		print(elemento)

