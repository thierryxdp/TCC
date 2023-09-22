def eh_quadrada(mat):
    for x in mat:
        for y in mat[0]:
            if len(mat[0]) == len(mat) or mat == []:
                return True
            else:
                return False