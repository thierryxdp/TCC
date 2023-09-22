def busca(setor,matriz):
    dados = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            cadastro = matriz[i]
            dados += cadastro[0:2] + [cadastro[3]]
    return dados