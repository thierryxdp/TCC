def busca(setor, matriz):
    lin = len(matriz)
    resp = []
    for i in range(0,lin):
        if setor in matriz[i][2]:
            list.append(resp, matriz[i][0])
            list.append(resp, matriz[i][1])
            list.append(resp,matriz[i][3])
    return [resp]