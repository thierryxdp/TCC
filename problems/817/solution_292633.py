def acima_da_media(lista:list) ->list:
    n = sum(lista)/len(lista)
    list.append(lista, n)
    list.sort(lista)
    if list.count(lista, n) == 2:
        return lista[list.index(lista,n)+2:
    else:
    	return lista[list.index(lista,n)+1:]