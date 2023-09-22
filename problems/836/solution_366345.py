def busca(palavra,matriz):
    resposta=[]
    for i in range(len(matriz)):
        resposta=[]+resposta
        for j in range(len(matriz[0])):
            if palavra in matriz[i]:
                list.append(resposta,matriz[i][j])
    return resposta