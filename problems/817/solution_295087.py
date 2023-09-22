def acima_da_media(lista):
    n = (sum(lista))/len(lista) + 0.0001
    list.append(lista, n)
    list.sort(lista)
    posicao = list.index(lista, n)
    l = lista[posicao+1:]
    return l