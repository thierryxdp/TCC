def faltante(L: List[int]):
    posicao = 0
    while L[posicao] < len(L):
        if posicao+1 == L[posicao]:
            posicao = posicao + 1
        break
    return posicao+1