def eh_quadrada(mat):
    '''a funç˜ao booleana para identificar se uma matriz é quadrada.
       list->bool'''
    soma=0
    nLin=len(mat)
    nCol=len(mat[0])
    for i in range(nLin):
        for j in range(nCol):
            soma+=soma
    if nLin==nCol or nLin>0:
        return True
    else:
        return False