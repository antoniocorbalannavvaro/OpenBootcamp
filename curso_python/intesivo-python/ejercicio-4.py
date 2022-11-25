'''
Enunciado: Utilizando la API de https://openweathermap.org/ y realizando una petición a 
https://api.openweathermap.org/data/2.5/weather?q={city%20name}&appid={API%20key}, 
obtén la temperatura máxima y mínima, para la ciudad que proporcione el usuario.

Objetivo:

Aprender a utilizar librerías externas (en este caso, requests)

Manipular el resultado de la petición (JSON)
'''

import requests

response = requests.get("http://api.open-notify.org/astros.json")
print('STATUS:', response)

def get_data(value):
    
    names = []
    content = list(response.json().values())[1]

    for i in content:
        names.append(list(i.values())[value])
    
    return names

names = get_data(0)
craft = get_data(1)

print(names)
print(craft)