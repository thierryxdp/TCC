import math
def acima_da_media(lista):
    '''retorna uma lista com as notas acima da media; list -> list'''
    media = sum(lista)/len(lista)
    a = list.sort(lista)
    b = math.floor(media) + 1
    c = list.index(lista, b or b+1 or b+2 or b+3 or b+4)
    lista = lista[c:]
    return lista