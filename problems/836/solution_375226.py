def busca(setor,matriz):
    informacoes = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.remove(matriz[i],setor)
            informacoes += [matriz[i],]
    return informacoes