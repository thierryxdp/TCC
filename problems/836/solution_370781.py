def busca(setor, matriz):
    resp = []

    for i in range(0, len(matriz)):
        teste = False
        for j in range(0, len(matriz)):
            if matriz[i][j] == setor:
                teste = True
        if teste == True:
            resp.append(matriz[i])
    if setor not in matriz[i]:
        return []     
    return resp