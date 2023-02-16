# EJEMPLOS DE EXPRESIONES REGULARES USANDO MATCH Y SEARCH
import re 

print("UTILIZANDO FUNCION MATCH BUSCANDO CARACTERES")

nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="sandra López"
nombre4="Jara López"
nombre5="Lara López"

# LA FUNCIO MATCH SOLO BUSCA AL COMIENZO DEL TEXTO

if re.match("Sandra",nombre1,re.IGNORECASE):
	print ("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")


if re.match("Sandra",nombre3,re.IGNORECASE):
	print ("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")

print("\nBusqueda utilizando comodin punto'(.)'")

# al utilizar (.) ".ara" esto indica que buscar todo lo que comience por caulquier caracter y que siga con "ara"
if re.match(".ara",nombre4,re.IGNORECASE):
	print ("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")


print("\nUTILIZANDO FUNCION MATCH BUSCANDO NUMEROS")

cadena1="Sandra López"
cadena2="67587876876"
cadena3="a8778756456"

# utilizando "\d" esto indica que buscar si el texto comienza con un numero
if re.match("\d", cadena1):
	print ("Hemos encontrado el numero")
else:
	print("No hemos encontrado el numero")

# utilizando "\d" esto indica que buscar si el texto comienza con un numero
if re.match("\d", cadena2):
	print ("Hemos encontrado el numero")
else:
	print("No hemos encontrado el numero")

# utilizando ".\d" esto indica que buscar si el texto comienza con cualquier caracter y luego con un numero
if re.match(".\d", cadena3):
	print ("Hemos encontrado el numero")
else:
	print("No hemos encontrado el numero")


print("\nUTILIZANDO FUNCION SEARCH")

# LA FUNCIO SEARCH BUSCA EN TODA LA CADENA DE TEXTO
if re.search("López",nombre1,re.IGNORECASE):
	print ("Hemos encontrado el apellido")
else:
	print("No hemos encontrado el apellido")

if re.search("López",nombre2,re.IGNORECASE):
	print ("Hemos encontrado el apellido")
else:
	print("No hemos encontrado el apellido")


