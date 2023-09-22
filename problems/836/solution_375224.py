def busca(setor,matriz):
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            informacoes += [matriz[i],]
    return informacoes