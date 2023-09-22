def eh_quadrada(mat):
    vazia = []
    if mat == vazia:
        return True
    if len(mat[0]) == len(mat):
        return True
    else:
        return False