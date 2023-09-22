def eh_quadrada(m):
	''' identifica se uma matriz é quadrada
    list(list) -> bool'''
    if len(m) == 0:
        return True
    if len(m[0]) == len(m):
        return True
    else:
        return False