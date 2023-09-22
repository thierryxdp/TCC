import math

def acima_da_media(lista):
    '''Retorna uma lista em ordem crescente com as notas que ficaram acima da média
    lista -> lista'''
    primlista = lista[:] #cópia
    x = sum(lista)
    a = len(lista)
    b = math.ceil(x/a)                  #valor médio
    list.append(lista, b)
    list.sort(lista)
    c = list.index(lista, b)
    d = lista[c+1:]
    e = round(len(lista)/2)
    f = lista[e]
    g = lista[c+2:]
    
    return primlista