def eh_quadrada(mat):
    '''função que retornar se uma matriz é quadrada ou não'''
    '''matriz-->bool'''
    if len(mat)==0:
        return True
    if len(mat)==len(mat[0]):
        return True
    else:
        return False