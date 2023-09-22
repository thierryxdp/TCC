import math
def acima_da_media(lista):
    media=math.ceil(sum(lista)/len(lista))
    list.append(lista,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    lista2=lista[:]
    list.remove(lista2,media)
    return lista2[posicao:]