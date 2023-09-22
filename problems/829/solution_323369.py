from random import randint
def soma_h(n):
    lista = []
    for numero in range(n):
        if numero <= n:
            h = (1 * (h**1/n - 1))/n - 1
        lista = lista + [h]
    return sum(lista)