#  Conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}

set1 = set(["dato1","dato2"])
# set2 = {set1, "dato3"} error

print(type(conjunto2))

# Teoria de conjuntos

conjunto3 = {1, 3, 5, 7}
conjunto4 = {1, 3, 7}

# verificamos si es un subconjunto
resultado1 = conjunto4.issubset(conjunto3)
resultadoCorto = conjunto4 <= conjunto3
print(resultado1)
print(resultadoCorto)
print("--------")

# verificamos si es un superconjunto
resultado = conjunto3.issuperset(conjunto4)
resultadoCorto = conjunto3 > conjunto4
print(resultado)
print(resultadoCorto)
print("--------")

# verificamos si dos conjuntos no son iguales
conjunto5 = { 8, 9, 2}
resultado = conjunto3.isdisjoint(conjunto5)
print(resultado)
print("--------")