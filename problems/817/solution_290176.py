def acima_da_media(lista):
    soma = sum(lista)
    media = ((soma)//(len(lista)))
    list.append(lista,media)
    list.sort(lista)
    posicao = list.index(lista,media)
	del lista[:posicao+1]
    if lista[0]==media:
        del lista[0]
    	return lista
    else:
        return lista