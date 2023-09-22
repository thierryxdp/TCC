def busca(setor, matriz):
    """..."""
    resp = []
    for i in range(0, len(matriz)):
        teste = False
        for j in range(0, len(matriz[i])):
            if matriz[i][j] == setor:
                teste = True
    if setor not in matriz[i]:
        return []
    return resp