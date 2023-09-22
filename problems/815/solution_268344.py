def insere(lista_numero,n):
    """insere um numero n na lista de forma ordenada"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero