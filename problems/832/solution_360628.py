def eh_quadrada(mat):
    ''''''
    lin = len(mat)
    col = len(mat[0])
    if len(mat) == 0:
        return True
    if lin == col:
        return True
    else:
        return False