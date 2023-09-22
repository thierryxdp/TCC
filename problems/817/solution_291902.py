import math
def acima_da_media(lista):

    media = sum(lista)/len(lista)

    list.sort(lista)

    lista_nova = lista[math.ceil(media):]

    return media