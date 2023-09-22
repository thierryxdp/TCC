def acima_da_media(lista):
    if len(lista) == 1:
        return []
    else:
    	media = sum(lista) / len(lista)
    	list.append(lista,media)
    	list.sort(lista)    
    	quantidade = len(lista)
    	menor = list.index(lista,media)
    	return lista[menor+1:quantidade]