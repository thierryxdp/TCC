def busca(setor,matriz):
    informacoes = []
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if setor == matriz[i][j]:
                informacoes.append(matriz[i])
            else:
                pass
        informacoes.remove(setor)
    return informacoes