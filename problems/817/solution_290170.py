def acima_da_media(lista):
    soma = sum(lista)
    media = ((soma)//(len(lista)))
    list.append(lista,media)
    list.sort(lista)
    posicao = list.index(lista,media)
	del lista[:posicao+1]
    del lista[posicao]
    return lista