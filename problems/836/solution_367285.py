def busca(nome,matriz):
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if nome not in matriz[i][j]:
                return dados
            if nome in matriz[i][j]:
                dados = matriz[i]
                
    return dados