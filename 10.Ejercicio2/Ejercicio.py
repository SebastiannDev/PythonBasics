# pedir el nombre y la edad de los compañeros que vinieron a clase

def obtener_compañeros(cantidad):
    compañeros = []

    for i in range(cantidad):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))

        compañeros.append(tuple((nombre, edad)))
    
    compañeros.sort(key= lambda x: x[1])

    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    return asistente, profesor

asistente, profesor  = obtener_compañeros(5)
print(f"El profesor es: {profesor} y su asistente es {asistente}")