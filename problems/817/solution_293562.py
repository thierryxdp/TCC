import math

def acima_da_media(lista):
    '''Retorna uma lista em ordem crescente com as notas que ficaram acima da média
    lista -> lista'''
    reglista = [1,3,5,7,9,11,13,15,17,19,21]
    primlista = lista[:] #cópia
    x = sum(lista)
    a = len(lista)
    b = math.ceil(x/a)                  #valor médio
    list.append(lista, b)
    list.sort(lista)
    c = list.index(lista, b)
    d = lista[c+1:]
    h = lista[0] + lista[-1]
    e = round(h/2)
    f = lista[e]
    g = lista[c+2:]

    if h == b and len(primlista) in reglista:
        return d
    else: 
        return d