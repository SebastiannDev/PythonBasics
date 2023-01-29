frase = input("Escribe una frase para calcular su tiempo de lectura:")

lista_palabras = frase.split()
cantidad_palabras = len(lista_palabras)

tiempo_dalto = (cantidad_palabras / 2) / 1.3

print(f'Has dicho: {cantidad_palabras} palabras, y tardarias: {cantidad_palabras / 2} segundos en decir.')
print(f'Dalto lo diria en: {round(tiempo_dalto, 2)} segundos')