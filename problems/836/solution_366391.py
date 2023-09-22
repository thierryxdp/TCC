def busca(palavra,matriz):
    resposta=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if palavra in matriz[i]:
                x=matriz[0][i]
                list.append(resposta,x)
    return resposta