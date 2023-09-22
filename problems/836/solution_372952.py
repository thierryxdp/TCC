def busca(setor,matriz):   
    dados_setor=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            list.append(dados_setor,matriz[i])            
    return dados_setor