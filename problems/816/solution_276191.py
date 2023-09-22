def maiores(lista,n):
    """coment"""
    lista_n=lista+[n]
    list.sort(lista_n)
    ind=list.index(lista_n,n)
    del lista_n(:(ind))
    return list_n