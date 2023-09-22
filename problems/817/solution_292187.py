from math import *
def acima_da_media(lista):
    media = sum(lista)/len(lista)
    lista = lista + [media]
    lista.sort()
    posi = list.index(lista, media)
    del lista[posi]
    return lista[:posi:-1]