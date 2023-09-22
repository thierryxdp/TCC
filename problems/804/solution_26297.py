#Start your python function heredef filtra_pares(x):

index = len(x)

i=0

lista = []

while i < index:

if x[i] % 2 == 0:

lista.append(x[i])

i+= 1

return tuple(lista)