def eh_quadrada(m):
    '''função que verifica se uma matrix é quadrada
    list-->bool'''
    if m == []:
        return True
    elif len(m) == len(m[0]):
        return True
    else:
        return False