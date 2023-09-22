def faltante(L):
    """
       """
    contador = 1
    posicao = 0
    while contador < len(L):
        if L[posicao] == contador:
            contador = contador + 1
        posicao = posicao + 1
    return contador