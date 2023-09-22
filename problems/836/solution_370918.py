def busca(setor, matriz):
    for i in range(0, len(matriz)):
        teste = False
        resp = []
        for j in range(0, len(matriz)):
            if matriz[i][j] == setor:
                teste = True
                resp.append(matriz[i])
    if teste == False:
        return []
    for i in range(0, len(resp)):
        for j in range(0, len(resp)):
            if resp[i][j] == setor:
                resp.remove(setor)
    return resp