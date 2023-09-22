def busca(setor,matriz):
    informacoes = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            informacoes += [matriz[i],]
    return informacoes