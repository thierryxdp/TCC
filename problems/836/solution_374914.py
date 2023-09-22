def busca(setor,matriz):
    """essa funcao recebe uma string e uma matriz e dado o nome de um setor da empresa, a funcao retorna uma lista com os dados de todos os funcion´arios daquele setor.
    str,list->list"""
    informacao=[]
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        if setor in matriz[i]:
            informacao.append(matriz[i])
            del informacao[i][j]
        if setor not in matriz[i]:
            i=i-1
    return informacao