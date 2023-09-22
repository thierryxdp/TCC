import math
def acima_da_media(lista):
    soma = sum(lista)
    media = math.floor((soma)/(len(lista)))
    list.append(lista,media)
    list.sort(lista)
    posicao = list.index(lista,media)
	del lista[:posicao+1]
    return lista