#gerador de senhas seguras

import random

letra_maiuscula = chr(random.randint(65, 90))
letra_minuscula = chr(random.randint(97, 122))
char_especial = chr(random.randint(33, 64))
lista_de_numeros = []

for i in range(5): #até 8 digitos
  numeros = random.randrange(9)
  lista_de_numeros.append(numeros) 
random.shuffle(lista_de_numeros)
lista_de_numeros = str(lista_de_numeros) [1:-1]
lista_de_numeros = lista_de_numeros.replace(',', '')

print(letra_maiuscula, letra_minuscula, lista_de_numeros, char_especial)