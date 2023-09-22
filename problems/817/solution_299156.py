import math
def acima_da_media (lista):
    qtd=len(lista)
    soma=sum(lista)
    media = math.floor(soma/qtd)
    if (media in lista):
        lista.append(media)
        list.sort(lista)
        nindex = lista.index (media)+2
        return lista[nindex:]
    else:
        lista.append(media)
        list.sort(lista)
    	nindex = list.index (lista, media)+1
    	return lista[nindex:]