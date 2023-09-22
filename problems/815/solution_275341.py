def insere(lista_numero,n):
    """
    adiciona um numero e depois ordena em ordem creescente
    """
    lista=lista_numero+[n]
    lista=list.sort(lista)
    return lista