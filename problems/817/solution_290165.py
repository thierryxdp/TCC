import math
def acima_da_media(lista):
    soma = sum(lista)
    media = math.ceil((soma)/(len(lista)))
    list.append(lista,media)
    list.sort(lista)
    posicao = list.index(lista,media)

    if list.count(lista,media)>=2:
        del lista[:posicao+2]
        return lista
    else:
        del lista[:posicao+1]
        return lista