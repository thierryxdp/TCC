def insere(lista_numero,n):
    """Inserte um intem e ordena a lista dada na entrada; list, int ==>list"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero