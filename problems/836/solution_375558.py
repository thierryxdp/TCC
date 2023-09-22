def busca(setor, matriz):
    lin = len(matriz)
    resp = []
    for i in range(0,lin):
        if setor in matriz[i][2]:
            list.append(resp, matriz[i])
    return resp