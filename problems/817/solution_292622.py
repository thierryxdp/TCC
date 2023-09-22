def acima_da_media(lista:list) ->list:
    n = int((sum(lista))/len(lista))
    list.append(lista, n)
    list.sort(lista)
    return lista[list.index(lista,n)+1:]