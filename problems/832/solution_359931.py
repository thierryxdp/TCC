def eh_quadrada(mat):
    '''função booleana que identifica se uma matriz(mat) é quadrada
    ou não. list->bool'''
    if len(mat) ==0 or len(mat)==len(mat[0]):
        return True
    else:
        return False