def eh_quadrada(mat):
    if mat == []:
        return True
    else:
    	l1 = len(mat[0])
    l2 = len(mat)
    if l1 == l2:
        return True
    else:
        return False