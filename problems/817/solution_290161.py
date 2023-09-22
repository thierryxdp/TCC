import math
def acima_da_media(lista):
    soma = sum(lista)
    media = math.ceil((soma)/(len(lista)))
    list.append(lista,media)
    list.sort(lista)
    posicao = list.index(lista,media)
	del lista[:posicao+1]
    return list.count(lista,media)