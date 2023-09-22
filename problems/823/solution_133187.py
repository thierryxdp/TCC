def faltante(lista):
    """ """
    """ """
    
    i = 0
    listacerta = list(range(1,len(lista)))
    while i < len(lista):
        if lista[i] != listacerta[i]:
            return i + 1
        i = i + 1