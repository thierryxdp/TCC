def filtra_pares(tupla:tuple) ->tuple:
    """
    filtra os elementos pares de uma tupla
    """
    if tupla[0]%2 == 0 and tupla[1]%2 == 0:
        return tupla[0],tupla[1]