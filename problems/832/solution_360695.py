def eh_quadrada(m):
    '''Função que receba uma matriz e identifica se é quadrada
    list -> bool'''
    if len(m) == 0:
        return True
	if len(m) == len(m[0]):
        return True
    else:
        return False