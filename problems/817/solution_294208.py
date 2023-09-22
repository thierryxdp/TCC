import math
def acima_da_media(lista_notas):
    list.sort(lista_notas)
    media = math.floor(len(lista_notas))
    del lista_notas[0:media]
    return lista_notas