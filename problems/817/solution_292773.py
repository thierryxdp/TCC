import math
def acima_da_media(lista):

    media = sum(lista)/len(lista)

    if media in lista:
        list.sort(lista)
        indice_media = list.index(lista,media)
        return lista[indice_media+1:]
    

    else:
        list.append(lista,media)
        list.sort(lista)
        indice_media = list.index(lista,media)
        return lista[indice_media+1:]