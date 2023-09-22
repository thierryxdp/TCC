def eh_quadrada(mat):
    for x in mat:
        for y in mat[x]:
            if len(mat[x]) == len(mat):
                return True
            else:
                return false