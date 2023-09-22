def busca(setor, matriz):
    """A função recebe como entrada uma string e uma matriz
    cujos elementos são strings, e retorna outra matriz cujos
    elementos são strings."""
    for informacao in matriz:
        if informacao[2] == setor:
            return [[informacao[0], informacao[1], informacao[3]]]