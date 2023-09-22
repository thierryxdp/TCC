def bolos(A,B,C):
    quantidadeMinimafarinha = A//2
    quantidadeMinimaovos = B//3
    quantidadeMinimaleite = C//5
    return min(quantidadeMinimafarinha, quantidadeMinimaovos, quantidadeMinimaleite)