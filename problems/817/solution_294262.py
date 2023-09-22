import math
def acima_da_media(lista_notas):
    '''define as notas acima da media
    	list -> list'''
    list.sort(lista_notas)
    media = math.ceil(len(lista_notas)/2)
    del lista_notas[0:media]
    return lista_notas