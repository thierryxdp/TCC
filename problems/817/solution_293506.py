import math

def acima_da_media(lista):
    '''Retorna uma lista em ordem crescente com as notas que ficaram acima da média
    lista -> lista'''
    primlista = [0,2,4,6,8,10,12,14] #lista par
    seglista = [1,3,5,7,9,11,13] #lista ímpar
    x = sum(lista)
    a = len(lista)
    b = math.ceil(x/a)                  #valor médio
    list.append(lista, b)
    list.sort(lista)
    c = list.index(lista, b)
    d = lista[c+1:]
    return d