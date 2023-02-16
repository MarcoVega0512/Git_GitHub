# EJEMPLOS DE EXPRESIONES REGULARES
import re 

cadena="Vamos a aprender expresiones regulares e Python. Python es un lenguaje de sintaxis sencilla"

# el metodo search busca una palabra dentro de un texto, tiene dos parametros
# el primero es la palabra a buscar y el segundo en donde se debe buscar
print(re.search("aprender",cadena))  # si la busqueda es correcta devuelve un objeto de tipo Match

print(re.search("python",cadena))  # si la busqueda es incorrecta devuelve un valor "None"

textoBuscar="aprender"

if re.search(textoBuscar,cadena) is not None:
	print("He encontrado el texto")
else:
	print("No he encontrado el texto")

# busca el texto en la cadena y el resultado lo deja en una variable
textoEncontrado=re.search(textoBuscar,cadena)

# con el metodo start() indica la posicion inicial donde se encuentra la palabra en el texto
print(textoEncontrado.start())

# con el metodo end() indica la posicion final donde se encuentra la palabra en el texto
print(textoEncontrado.end())

# con el metodo span() indica la posicion inicial y final donde se encuentra la palabra en el texto
print(textoEncontrado.span())

textoBuscar2="Python"

# con el metodo findall() devuelve una lista con las veces que esta la palabra en el texto
print(re.findall(textoBuscar2,cadena))

# con el metodo len() devuelve la cantidad de veces (en numero) que encontro la palabra en el texto
print(len(re.findall(textoBuscar2,cadena)))


