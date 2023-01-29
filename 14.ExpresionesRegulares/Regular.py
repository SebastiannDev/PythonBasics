import re

texto = "Este mensaje es autogenerado para regex, 1, en estos casos el Mensaje[2] se usa para fines academicos(linea 3)     "

resultado = re.search("mensaje", texto)
print(resultado)
print("-------")

resultado = re.findall("mensaje", texto, flags = re.IGNORECASE)
print(resultado)
print("-------") 

# \d -> busca digitos numericos
resultado = re.findall(r"\d", texto)
print(resultado)
print("-------")

# \D -> busca todo menos dígitos numéricos del 0 - 9
resultado = re.findall(r"\D", texto)
print(resultado)
print("-------")

# \w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w", texto)
print(resultado)
print("--- \w ----")

# \W -> busca todo menos caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W", texto)
print(resultado)
print("--- \W ----")

# \s -> busca espacios en blanco 
resultado = re.findall(r"\s", texto)
print("--- \s ----")

# \S -> busca todo excepto espacios en blanco 
resultado = re.findall(r"\S", texto)
print("---- \S ---")

# Verificando si un email es valido:
email = "anon@mail.to"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
result = re.match(pattern, email)

print("Direccion de correo válida") if result else print("Direccion de correo invalida")
