def eh_quadrada(mat):
    '''Retorna True se a matriz for quadrada (mesma quantidade
    de linhas e colunas) e False caso não seja
    list -> bool '''
    lin = len(mat)
    if lin == 0:
        return True
    col = len(mat[0])
    if lin == col:
        return True
    else:
        return False