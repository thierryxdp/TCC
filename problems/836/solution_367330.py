def busca(nome,matriz):
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if nome in matriz[i][j]:
                dado += matriz[i]
                d = list.index(dado,nome)
                del dado(d)
                dados += dado
            if nome not in matriz[i][j]:
                dados = dados
    return dados