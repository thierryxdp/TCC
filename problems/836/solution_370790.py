def busca(setor, matriz):
    linhas = len(matriz)
    saida = []
    for i in range(linhas):
        if setor == matriz[i][2]:
            saida.append([matriz[i][0], matriz[i][1], matriz[i][3]])
    return saida