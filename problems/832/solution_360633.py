def eh_quadrada(mat):
    ''''''
    lin = len(mat)
    if lin == 0:
        return True
    col = len(mat[0])
    if lin == col:
        return True
    else:
        return False