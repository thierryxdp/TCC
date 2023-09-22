def busca(setor,matriz):
    resposta=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            x=matriz[i][:2]+matriz[i][3:]
            list.append(resposta,x)
    return resposta