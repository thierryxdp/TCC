def insere(lista,n):
    """funçao que inclui a entrada n na posiçao correta 
    mantendo a lista_numero ordenada
    str->str"""
    lista.insert(0,n)
    lista.sort()
    return lista