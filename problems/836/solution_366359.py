def busca(palavra,matriz):
    resposta=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if palavra in matriz[i]:
                resposta=[]+resposta
                list.append(resposta,matriz[i][j])
                resposta=resposta
            if palavra not in matriz[i]:
                resposta=[resposta]
    return resposta