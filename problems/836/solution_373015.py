def busca(setor,matriz):
    informacao=[]
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        if setor in matriz[i]:
            informacao.append(matriz[i])
    for j in range(len(informacao)): 
        del informacao[j][2]
    return informacao