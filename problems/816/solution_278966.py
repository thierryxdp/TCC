def maiores(lista:list, n:int) ->list:
    list.append(lista, n)
    list.sort(lista)
    return lista[list.index(lista,n):]