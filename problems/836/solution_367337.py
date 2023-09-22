def busca(nome,matriz):
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if nome in matriz[i][j]:
                dados += [[matriz[i][0],matriz[i][1],matriz[i][3]]]
                 
            if nome not in matriz[i]:
                dados = dados
    return dados