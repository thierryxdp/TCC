def eh_quadrada(mat):
    ''' funcao identifica se uma matriz é quadrada'''
    if len(mat)==0:
        return True
    linhas= len(mat)
    coluna= len(mat[0])
    return coluna==linhas