def insere(lista,n):
    """Função que dada uma lista e um elemento "n", insere "n" na lista na posição correta de forma ordenada. str -> str"""
    lista.insert(0,n)
    lista.sort()
    return lista