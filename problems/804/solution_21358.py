def filtra_pares (tupla): # a tupla de entrada irá possuir 4 elementos
    """
    Essa função tem como entrada uma tupla com 4 elementos e ira retornar uma nova
    tupla que contenha somente os elementos pares da tupla original.
    tuple->tuple
    """
    if tupla[0] % 2 == 0 and tupla[1] % 2 != 0 and tupla[2] % 2 != 0 and tupla[3] % 2 != 0:
        return tuple(tupla [0])
    
    elif tupla[1] % 2 == 0 and tupla[0] % 2 != 0 and tupla[2] % 2 != 0 and tupla[3] % 2 != 0:
        return tuple(tupla[1])
    
    elif tupla[2] % 2 == 0 and tupla[0] % 2 != 0 and tupla[1] % 2 != 0 and tupla[3] % 2 != 0:
        return tuple(tupla[2])
    
    elif tupla[3] % 2 == 0 and tupla[0] % 2 != 0 and tupla[1] % 2 != 0 and tupla[2] % 2 != 0:
        return tuple(tupla[3])