def busca(setor,matriz):
    dados=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            list.pop(matriz[i],2)
            dados.append(matriz[i])
    return dados