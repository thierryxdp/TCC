import math
def acima_da_media(lista):
    '''retorna uma lista com as notas acima da media; list -> list'''
    media = sum(lista)/len(lista)
    a = list.sort(lista)
    b = math.floor(media)
    lista = lista[b+1:]
    return lista