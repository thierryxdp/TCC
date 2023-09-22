def maiores(lista,n):
    """..."""
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    ind=list.index(lista,n)
    listaf=lista[ind+1:]
    return listaf