def faltante(lista):
    """
    """
    Y=lista[:]
    list.sort(Y)
    cont = 0
    peca = -1
    while cont < len(Y):
        if Y[cont]==cont+1:
            cont += 1
        else:
            peca = cont+1
            cont = len(Y)
    if peca == -1:
        peca = len(Y) + 1
        
    return peca