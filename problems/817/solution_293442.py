import math

def acima_da_media(lista):
    '''Retorna uma lista em ordem crescente com as notas que ficaram acima da média
    lista -> lista'''
    x = sum(lista)
    a = len(lista)
    b = x/a
    list.append(lista, b)
    list.sort(lista)
    y = list.index(lista, b)
    z = lista[y+1:]
    d = lista[z+1:]
    f = math.ceil(len(lista)/2)
    g = lista[f]
  
    if b == g:
        return d
    else:
        return z