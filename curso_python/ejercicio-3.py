#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. Tienes que subir capturas de pantalla en una carpeta comprimida zip.
# IMC = peso en kilogramos dividido por la estatura en metros cuadrados.

weight, height = input('¿Cuál es tu peso y tu altura (Introdúcelos separados por comas):').split(',')

imc = round(float(weight) / (float(height) ** 2), 2)

print(f'Tu índice de masa corporal es {imc}')
