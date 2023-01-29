numeros = [1, 5, 10, 15, 20]

print(list(numero * 2 for numero in numeros))
print("---------")

numeros_pares = list(filter(lambda numero: numero % 2 == 0, numeros))
print(numeros_pares)