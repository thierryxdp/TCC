def busca(setor,matriz):
    informacoes = []
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if setor == matriz[i][j]:
                informacoes.append(matriz[i])
                informacoes.remove(matriz[2])
            else:
                pass
    return informacoes