# List -> crea una lista
lista = list(["Hola", "Ada", 31, 32, 33, True])

# Len -> cuenta la cantidad de elementos de una lista
cantidad_elem = len(lista)
print(cantidad_elem)
print("-------------")

# Append -> agrega un elemento a la lista
lista.append("nuevo elemento")
print(lista)
print("-------------")

# Insert -> agrega un elemento a la lista en el indice especificado
lista.insert(1, "estimada")
print(lista)
print("-------------")

# Extend -> agrega varios elementos a la lista
lista.extend([666, "Nuevo orden"])
print(lista)
print("-------------")

# Pop -> Elimina un elemento de una lista, pide indice y devuelve valor
lista.pop()
print(lista)
print("-------------")

# Remove -> remuevel un elemento de una lista
lista.remove("nuevo elemento")
lista.remove("Hola")
lista.remove("estimada")
lista.remove("Ada")
print(lista)
print("-------------")

# Sort -> ordena una lista ASC / DSC
lista.sort()
print(lista)
print("-------------")

# Reverse -> invierte los elementos de una lista
lista.reverse()
print(lista)
print("-------------")

# Index
elemento_lista = lista.index(True)
print(elemento_lista)
print("-------------")

# Clear -> elimina los elementos de una lista
lista.clear()
print(lista)
print("-------------")
