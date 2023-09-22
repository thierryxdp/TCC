def eh_quadrada(mat):
    if len(mat) == 0:
        return 'True'
    if len(mat) == len(mat[0]):
        return True
    else:
        return False