def eh_quadrada(mat):
    '''função que identifica se uma matriz é quadrada'''
    lin = len(mat)
    if lin == 0:
        return True
    col = len(mat[0])
    if lin == col:
        return True
    else:
        return False