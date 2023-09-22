def acima_da_media(lista):
	list.sort(lista)
    if (len(lista)%2) == 0:
        return lista[(len(lista)//2):]
    else:
        return lista[((len(lista)//2)+1):]