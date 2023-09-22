def busca(setor,matriz):
    informacoes = []
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if setor == matriz[i][j]:
                informacoes.append([matriz[i][0], matriz[i][1], matriz[i][3]])
            else:
                pass
    return informacoes