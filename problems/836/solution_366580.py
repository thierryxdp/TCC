def busca(string,matriz):
    dados = []
    for i in range(len(matriz)):
        if string in matriz[i]:
            a = matriz[i][2]
            list.remove(matriz[i],a)
            dados += [matriz[i]]
    return dados