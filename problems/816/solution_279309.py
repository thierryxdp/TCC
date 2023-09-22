def maiores(lista,n):
    """Função que dada uma lista e um numero n retorna outra lista.List-->List """
    lista.append(n)
    lista.sort()
    pos = lista.index(n)
    return lista[pos+1:]