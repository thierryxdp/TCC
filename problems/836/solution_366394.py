def busca(palavra,matriz):
    resposta=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if palavra in matriz[0][j]:
                x=matriz[:][i]
                list.append(resposta,x)
    return resposta