from math import *
def acima_da_media(lista):
    media = sum(lista)/len(lista)
    lista = lista + [media]
    lista.sort()
    posi = list.index(lista, media)
    del lista[posi]
    if(list.count(lista, media) >0):
        list.remove(lista, media)
    return lista[:posi]