def busca(nome,matriz):
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if nome in matriz[i][j]:
                dados = dados + [matriz[i]]
                del dados[j]
            if nome not in matriz[i][j]:
                dados = dados
    return dados