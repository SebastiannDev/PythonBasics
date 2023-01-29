diccionario = {
    "nombre": "Abraham",
    "apellido": "Lincon",
    "subs": 99999
}

# keys -> devuelve las claves
print(diccionario.keys())
print("---------")

# get -> devuelve los elementos
print(diccionario.get("subs"))
print("-------------")

# pop -> elimina un elemento
print(diccionario.pop("subs"))
print(diccionario)
print("-------------")

# items -> para iterar el diccionario
print(diccionario.items())
print("-------------")

# clear -> elimina los elementos
diccionario.clear()
print(diccionario.items())