def insere( lista_numero, n) :
    """list,int -> list"""
    """recebe uma lista e insere um numero nela de forma que continue ordenada crescentemente"""
    
    lista_numero += [n]
    list.sort(lista_numero)
    
    return lista_numero