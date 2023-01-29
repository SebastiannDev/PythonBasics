animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [22, 11, 33]

# recorriendo lista
for animal in animales:
    print(animal)
print("--------")

for numero in numeros:
    print(numero * 2)
print("--------")

for numero, animal in zip(numeros, animales):
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo lista 2: {animal}')
print("--------")

for num in range(5, 11):
    print(num)
print("--------")

for num in enumerate(numeros):
    print(f'Indice: {num[0]}, Valor: {num[1]}')
print("--------")

# for else
for num in numeros:
    print(f'valor actual: {num}')
else:
    print("El bucle termino...")
    print("--------")

diccionario = dict(nombre = "Lucas", apellido = "Monroi", subs = 566)

for datos in diccionario.items():
    print(f'la clave es: {datos[0]}, el valor es: {datos[1]}')
print("--------")

for datos in diccionario:
    print(f'los datos son: {datos}')
print("--------")

# en una sola linea:
numerosDup = [numero * 2 for numero in numeros]
print(numerosDup)
print("--------")
