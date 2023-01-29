import pandas as pd

df = pd.read_csv("./13.Pandas/data.csv")
print(df)
print("------")

# slice / slicing -> permite identificar un rango de datos determinado
cadena = "0123456789"
print(cadena[2:])
print("---------")

# Ordernar dataframe por edad
print(df.sort_values("edad"))
print("--------")

print(df.sort_values("edad", ascending=False))
print("--------")