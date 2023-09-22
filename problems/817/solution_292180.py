def acima_da_media(lista):
    from math import *
    media = sum(lista)/len(lista)
    return lista[ceil(media):]