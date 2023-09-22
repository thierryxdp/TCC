def bolos (A, B, C):
    """Calcula a quantidade de bolos que podem ser feitos com a quantidade de
    ingredientes dada
    entrada: int, int, int
    saida: int
    """
    quantidadeMinimafarinha = A//2
    quantidadeMinimaovos = B//3
    quantidadeMinimadeleite = C//5
    return max(quantidadeMinimafarinha, quantidadeMinimaovos, quantidadeMinimaleite)