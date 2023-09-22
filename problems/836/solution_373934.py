def busca(setor,matriz):
    ''' '''
    dados=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            return dados.append(matriz[i])