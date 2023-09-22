def acima_da_media(lista):
	""" A função retorna uma lista com notas acima da media;
    list -> list """
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    ind = list.index(lista,media)    
    return lista[ind+1:]