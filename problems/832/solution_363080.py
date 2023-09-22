def eh_quadrada(mat):
    for x in mat:
        for y in x:
            if len(mat) == len(x) or len(mat) == 0:
                return True
            else:
                return False