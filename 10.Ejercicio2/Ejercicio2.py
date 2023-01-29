# crea una funcion que devuelva los numeros primos
# entre 0 y el argumento dado

def numeros_primos(cantidad):
    lista_numeros_primos = []
    for i in range(cantidad + 1):
        if i % 2 != 0:
            lista_numeros_primos.append(i)
    return lista_numeros_primos


print(numeros_primos(13))
