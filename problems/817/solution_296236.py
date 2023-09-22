import math
def acima_da_media(lista):
    '''retorna uma lista com as notas acima da media; list -> list'''
    media = sum(lista)/len(lista)
    a = list.sort(lista)
    b = math.floor(media) + 1
    c = list.index(lista, >=b)
    lista = lista[c:]
    return lista