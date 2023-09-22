def filtraMultiplos(lista, n):
    """ """
    """list, int -> list"""
    multiplos = list()
    i = 0
    
    while (i < len(lista)):
        if lista[i] % n == 0:
            list.append(multiplos,lista[i])
        
        i = i + 1
        
        return multiplos