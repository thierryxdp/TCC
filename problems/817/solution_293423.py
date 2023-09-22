import math

def acima_da_media(lista):
    '''Retorna uma lista em ordem crescente com as notas que ficaram acima da média
    lista -> lista'''
    x = sum(lista)/len(lista)
    list.append(lista, x)
    list.sort(lista)
    y = list.index(lista, x)
    z = lista[y+1:]
    return lista