def eh_quadrada(mat):
    for x in mat:
        for y in x:
            if len(mat) == len(x) or mat == []:
                return True
            else:
                return False