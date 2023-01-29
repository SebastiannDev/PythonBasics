# creando diccionarios
diccionario = dict(nombre = "Agust", apellido = "Morgan")
print(diccionario)
print("---------")

# las listas no pueden ser claves y usamos frozenset para ingresar conjuntos
diccionario = {frozenset(["hola","mundo"]): "test"}
print(diccionario)
print("---------")

# creando un diccionario con fromkeys, al ser key, value, quedan en default
diccionario = dict.fromkeys(["nombre", "apellido", "suscriptores"])
print(diccionario)
print("---------")

diccionario = dict.fromkeys(["nombre", "apellido"])
print(diccionario)
print("---------")

diccionario = dict.fromkeys(["nombre", "apellido"], "etc...")
print(diccionario)
print("---------")
