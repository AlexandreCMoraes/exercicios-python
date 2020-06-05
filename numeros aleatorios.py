import random


lista = [6,45,9]

#random.seed(1) #da o mesmo resultado
numero = random.randint(0,10)#imprime um numero aleatorio
print(numero)


numero = random.choice(lista)#escolhe um numero da lista aleatorio
print(numero)

