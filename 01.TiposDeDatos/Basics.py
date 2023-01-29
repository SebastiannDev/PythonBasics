# === Tipos de datos ===
Integers = 1
Flotantes = 2.1
Strings = "Hola mundo"

# === Datos compuestos ===
# listas: pueden ser modificados y aceptan diferentes tipos de datos
lista = ["Hola mundo", True, 1.73]

# tuplas: aceptan diferentes tipos de datos pero no se pueden modificar
tupla = ("Marco", "mosser", True, 2.3)


# conjuntos: no se pueden acceder por su indice, son desordenados y no aceptan valores duplicados.
conjunto = {"Rousee", "Morgan", False, 27.2, "Rousee"}

# diccionario: estan compuestos por clave, valor, estos son establcedios y se acceden desde su clave.
diccionario = {
    "nombre": "Miracles",
    "apellido": "Turso",
    "edad": 23
}

print(lista)
print("--------------")

print(tupla[1])
print("--------------")

print(conjunto)
print("--------------")

print(diccionario["nombre"])
print("--------------")


# === operadores aritmeticos ===

suma = 2 + 5
resta = 3 - 1
multiplicacion = 3 * 3
division = 8 / 2
exponente = 3 ** 3

# redondea los decimales hacia el minimo
division_baja = 12 // 5

resto = 12 % 5

print(f'Operadores Aritmeticos: la suma: {suma}, la resta: {resta}, la multiplicacion: {multiplicacion}, la division: {division}, el exponente: {exponente}, la division baja: {division_baja}, el resto: {resto}')
print("--------------")

# === Operadores ===

igual_que = 5 == 6
distinto_de = 5 != 6
mayor_que = 5 < 6
menor_que = 3 > 4
mayor_o_igual = 5 >= 6
menor_o_igual = 3 <= 5

print(
    f'Operadores Compración: igual que: {igual_que}, distinto de: {distinto_de}, mayor que: {mayor_que}, menor que: {menor_que}, mayor o igual: {mayor_o_igual}, menor o igual: {menor_o_igual}')
print("--------------")


# === Condicionales ===
cantidad = 5_000

if cantidad > 10_000:
    print("su saldo es mayor a la media")
    print("--------------")

elif cantidad > 8_000:
    print("usted tiene suficiente saldo")
    print("--------------")
else:
    print("Su saldo es insuficiente")

# === Operadores Logicos ===

# AND
resultado = True & True

# OR
resultado1 = True | False

# NOT
resultado2 = not True
