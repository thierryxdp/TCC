def filtra_pares(tupla:tuple) ->tuple:
    """
    filtra os elementos pares de uma tupla
    """
    if tupla[0] %2 == 0:
        return (tupla[0],)
    if tupla[1] %2 ==0:
        return (tupla[1],)
    if tupla[2] %2 == 0:
        return (tupla[2],)
    if tupla[3] %2 == 0:
        return (tupla[3],)
    if tupla[0] %2 == 0 and tupla[1] %2 == 0:
        return (tupla[0],tupla[1])
    if tupla[2] %2 == 0:
        return (tupla[2],)