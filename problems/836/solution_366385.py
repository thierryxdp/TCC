def busca(palavra,matriz):
    resposta=[]
    for i in range(len(matriz)):
        resultado=[]
        for j in range(len(matriz[0])):
            if palavra in matriz[i]:
                list.append(resultado,[matriz[i][j]])
                resposta=matriz[:][i]+resposta
    return resposta