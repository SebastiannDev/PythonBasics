archivo = open("./12.Archivos\\texto.txt", encoding="UTF-8")
# print(archivo.read())

print("--------")
# print(archivo.readline(10))
print("--------")

print(archivo.readlines())
archivo.close()