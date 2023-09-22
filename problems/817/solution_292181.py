from math import *
def acima_da_media(lista):
    media = sum(lista)/len(lista)
    return lista[ceil(media):]