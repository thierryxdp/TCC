def eh_quadrada(mat):
    '''Recebe uma matriz e retorna True caso ela seja
    quadrada. Se não, retorna False.
    list -> bool'''
    if len(mat) == 0:
        return True
    elif len(mat) == len(mat[0]):
        return True
    else:
        return False