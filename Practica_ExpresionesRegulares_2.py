# EJEMPLOS DE EXPRESIONES REGULARES USANDO ANCLA
import re 

lista_nombres=['Ana Gómez',
				'María Martín',
				'Sandra López',
				'Santiago Martín',
				'Sandra Fernandez']

print("Elementos que comiezan con el texto 'San'")				

for elemento in lista_nombres:

	# con el simbolo "^" (ancla) se indica que busque todos los elementos que comienzan con "San"
	if re.findall('^San',elemento): 

		print(elemento)

print("\nElementos que terminan con el texto 'Martín'")				

for elemento in lista_nombres:

	# con el simbolo "$" (ancla) se indica que busque todos los elementos que terminen con "Martín"
	if re.findall('Martín$',elemento): 

		print(elemento)

# EJEMPLOS DE EXPRESIONES REGULARES USANDO CLASE DE CARACTERES (PATRONES DE BUSQUEDA)

lista_nombres2=['hombres',
				'mujeres',
				'mascotas',
				'niños',
				'niñas']

print("\nElementos que contenga el comodin [ñ] en el texto")				

for elemento in lista_nombres2:

	# las clases de caracteres (patrones de busqueda o comodin) van entre corchetes"
	if re.findall('[ñ]',elemento): 

		print(elemento)

print("\nElementos que contenga mas de un comodin [oa] en el texto")				

for elemento in lista_nombres2:

	# con "niñ[oa]s" con este patron de busqueda buscara los elementos que contenga la palabra buscada"
	# que contenga una letra "o" o "a" en la posicion indicada
	if re.findall('niñ[oa]s',elemento): 

		print(elemento)
