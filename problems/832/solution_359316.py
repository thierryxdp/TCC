def eh_quadrada(mat):
    ''' função que dada uma lista (matriz) retornar se é quadrada ou não.
    list -> bool '''
    if len(mat) == 0:
        return True
    if len(mat) == len(mat[0]):
        return True
    else:
        return False