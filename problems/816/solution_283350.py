def maiores(lista_numero,n):
    """adicionamos o valor n na lista e depois fatiamos a nova lista
    no elemento n+1
    list, int -> list"""
    lista=lista_numero+[n]
    lista.sort()
    x=lista.index(n)
    return lista[x+1:]