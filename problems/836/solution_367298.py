def busca(nome,matriz):
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if nome in matriz[i][j]:
                list.append(dados, matriz[i])
                n = list.index(dados, nome)
                list.del(dados, n)
            if nome not in matriz[i][j]:
                dados = dados
    return dados