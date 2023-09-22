def faltante(L):
    """
       """
    contador = 1
    posicao = 0
    while contador <= len(L):
        if contador not in L:
            posicao= contador + posicao
        contador = L[contador-1]+1
    if posicao == 0:
        posicao = posicao + 1
    return posicao