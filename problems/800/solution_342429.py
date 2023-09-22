from random import randint
def total(lista, dicionario):
    a = len(lista)
    while lista in range(a):
        b = dict.get(dicionario, lista[a])
        a = a - 1
    return b