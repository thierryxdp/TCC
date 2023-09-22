def eh_quadrada(mat):
    for x in mat:
        for y in mat[0]:
            if len(mat[x]) == len(mat):
                return True
            else:
                return false