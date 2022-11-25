'''
Ejercicio 5

Enunciado: Convierte un Excel a CSV

Objetivo:

Aprender a trabajar con ficheros

Usar la librería pandas de Python
'''

import pandas as pd

df = pd.read_excel('file_example_XLS_1000.xls', index_col=0) 
df.to_csv('data.csv') 

print(df)