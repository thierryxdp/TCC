def busca(setor, matriz):
    """..."""
     resp = []
    for i in range(0, len(matriz)):
        teste = False
        for j in range(0, len(matriz[i])):
            if matriz[i][j] == setor:
                teste = True
        if teste == True:
            for i in range(0, len(matriz)):
                resp.append(0)
                resp[i] = []
                for j in range(0, len(matriz[j])):
                    if matriz[i][j] != setor:
                        resp[i].append(matriz[i][j])
    if setor not in matriz[i]:
        return []
    return resp