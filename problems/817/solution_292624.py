def acima_da_media(lista:list) ->list:
    n = sum(lista)/len(lista)
    if n not in lista:
    list.append(lista, n)
    list.sort(lista)
    return lista[list.index(lista,n)+1:]
	else:
        return lista[n+1:]