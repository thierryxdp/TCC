def busca(palavra,matriz):
    resposta=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if palavra in matriz[i]:
                list.append(resposta,matriz[i][j])
                list.remove(matriz,palavra)
    return resposta