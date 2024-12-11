import pandas as pd

# cargar el archivo con ruta 
df = pd.read_excel('C:/python/data_a_excel/paises.xlsx')

# iterar sobre las filas usando itertuples() mas eficiente
print("\nIterando con itertuples:")
for fila in df.itertuples(index=True, name='ExcelRow'):
    print(f'indice {fila.index}, datos {fila}')
    iteracion = fila.Index
    iso = fila.ISO
    nombre = fila.Nombre
