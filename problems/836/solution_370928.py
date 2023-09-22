def busca(setor, matriz):
    """..."""
    resp = []
    for i in range(0, len(matriz)):
        teste = False
        for j in range(0, len(matriz[i])):
            if matriz[i][j] == setor:
                teste = True
        if teste == False:
        return []
    for i in range(0, len(resp)):
        for j in range(0, len(resp)):
            if resp[i][j] == setor:
                resp.remove(setor)
    return resp