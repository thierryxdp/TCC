def eh_quadrada(x):
    '''função booleana que identifica se uma matriz é quadrada, bool->bool'''
    if len(x)==len(x[0]):
        return True
    else:
        return False