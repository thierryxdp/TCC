def faltante(lista):
    """ """
    """ """
    
    i = 0
    listacerta = list(range(1,len(lista)+1))
    while i < len(lista):
        if lista[i] != listacerta[i]:
            return i + 1
        if lista[-1] != listacerta[-1]:
            return listacerta[-1]
        i = i + 1