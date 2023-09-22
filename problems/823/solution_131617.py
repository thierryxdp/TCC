def faltante(L):
    """
       """
    contador = 1
    posicao = 0
    while contador <= len(L):
        if contador not in L:
            posicao= contador + posicao
    return contador = L[contador-1]+1