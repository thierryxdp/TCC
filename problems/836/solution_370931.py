def busca(setor, matriz):
    """..."""
    resp = []
    for i in range(0 , len(matriz)):
        for j in range(0, len(matriz[i])):
            if setor in matriz[i][j]:
                resp.append(matriz[i][j])
    return resp