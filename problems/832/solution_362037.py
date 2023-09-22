def eh_quadrada(m):
    '''função identifica se uma matriz é quadradada ou não'''
    if len(m)==0:
        return True
    else:
        return len(m)==len(m[0])