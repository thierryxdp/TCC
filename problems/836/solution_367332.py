def busca(nome,matriz):
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if nome in matriz[i]:
                dados += matriz[i]
                 
            if nome not in matriz[i]:
                dados = dados
    return dados