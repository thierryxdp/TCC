def busca(palavra,matriz):
    resposta=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if palavra in matriz[i]:
                list.remove(matriz[i][j],palavra)
                list.append(resposta,matriz[i][j])
                
    return resposta