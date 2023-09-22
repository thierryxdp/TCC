def busca(setor,matriz):
    for i in matriz:
        if matriz[i][2] == setor:
            informacoes += [matriz[i],]
    return informacoes