def eh_quadrada(mat):
    '''funcao que identifica se uma matriz é quadrada;
    list->bool'''
    f= mat[0]
    if len(f)==len(mat):
        return True
    elif len(mat)==[]:
        return True   
    else:
        return False