def faltante(L):
    L.sort()
    posicao = 0
    while posicao < len(L):
        if posicao+1 != L[posicao]:
            return posicao+1
        posicao = posicao + 1
    return posicao +1