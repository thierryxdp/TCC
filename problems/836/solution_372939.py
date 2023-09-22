def busca(setor,matriz):   
    dados_setor=[]
    i=0
    while i<len(matriz):
        if matriz[i][2]==setor:
            list.append(dados_setor,matriz[i:i+1])
        return dados_setor