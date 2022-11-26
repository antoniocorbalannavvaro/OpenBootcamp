'''
Ejercicio 6

Enunciado: Crea una función que convierta un password (entre 6 y 12 caracteres) 
en una cadena de texto alfanumérica de 32 caracteres. 
La función SIEMPRE debe devolver el mismo resultado para la misma entrada.

Objetivo:

Aprender a manejar los bucles y las cadena de texto.

Mejorar la capacidad algorítmica.
'''

symbols = '\':IA"Ne)@Y2x4[3~5\<|b€EJH1W MKkFr,t(wS8g*Q]p}0&VBD-TGlm!`=%ji_R;6#Od?qL/.Py>+s|CzZ{of^9uh7a$UXcnv'

def password_obfuscator(password):
    
    #Input check:
    if type(password) != str:
        return 'Invalid input. Only strings are supported'
    
    if len(password) < 6 or len(password) > 12:
        return 'Password length must be between 6 and 12'
    
    for i in password:
        if i not in symbols:
            return 'Some characters in your password are not supported'
    
    #Function:
    password = str(password)
    new_password = []
    
    for i in password:            
        new_password.append(symbols[symbols.index(i) - 1])
        
    try:
        index = symbols.index(new_password[-1])
    
    except:
        index = symbols.index(new_password[1])

    while len(new_password) < 32:
        try:
            new_password.append(symbols[index])
            index -= 3
        except:
            new_password.append(symbols[index])
            index += 3
            
    initial_password = new_password[0:len(password) + 1]
    generated_characters = new_password[len(password) + 1:]
    #new_password=''.join(new_password)
    
    print('initial_password',initial_password)
    print('generated_characters',generated_characters)
    
    count = 1
    
    for i in range(len(initial_password)):
        generated_characters.insert((count),initial_password[i])
        count += 3

            
    generated_characters = ''.join(generated_characters)
    
    return generated_characters


result1 = password_obfuscator('securepass')
result12 = password_obfuscator('securepass')
result2 = password_obfuscator('74ufjcn23TTs')
result3 = password_obfuscator('111111111')


print(result1)
print(len(result1))

print(result12)
print(len(result12))

print(result2)
print(len(result2))

print(result3)
print(len(result3))

'''
#Script para desordenar el string de symbols:

import random

symbols = '!@#$%`\'^&*( )-=[];,./\\|_+{}:"<>?|0123456789qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
random_sample = random.sample(symbols, len(symbols))

result = ''.join(random_sample)

print(result)
print(len(result))
print(len(symbols))
'''