import math
def acima_da_media(lista):
    if (len(lista) == 1):
        lista= []
        return lista
	media = sum(lista)/len(lista)
    math.ceil(media)
    int(media)
    lista.append(media)
    lista.sort()
    index = lista.index(media)
    lista.remove(media)
	return lista[index:]