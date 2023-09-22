def eh_quadrada(m):
    '''Esta função identifica se uma matriz é quadrada.
list(list) --> bool
'''
    print(len(m),len(m[0]))
    if len(m) == 0:
        return True
    if len(m) == len(m[0]):
        return True
    else:
        return False