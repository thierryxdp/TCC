def maiores(lista,n):
    """REcebe uma lista com numeros ordenados e um número n e devolve uma outra lista com todos os numeros acima desse numero n;
    	list, num -> list"""
    lista=list.append(lista,n)
    lista=list.sort(lista)
    listanova=lista[n:]
    return listanova