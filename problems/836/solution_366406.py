def busca(palavra,matriz):
    resposta=[]
    resultado=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if palavra in matriz[:][i]:
                x=matriz[:][i]
                list.append(resposta,x)
                resposta=resultado+resposta
    return resposta