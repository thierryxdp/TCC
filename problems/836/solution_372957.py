def busca(setor,matriz):   
    dados_setor=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            list.append(dados_setor,matriz[i])
            list.remove(dados_setor,dados_setor[i][2])
    return dados_setor