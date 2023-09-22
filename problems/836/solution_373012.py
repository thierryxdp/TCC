def busca(setor,matriz):
    informacao=[]
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        if setor in matriz[i]:
            informacao.append(matriz[i])
        del informacao[0][2]
        del informacao[1][2]
    return informacao