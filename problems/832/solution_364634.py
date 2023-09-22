def eh_quadrada(m):
    """Função que recebe uma matriz e informa se ela
é quadrada ou não
signature: matrix --> bool
"""
    lin = 0
    col = 0
    for i in range(len(m)):
        lin += 1
    for i in range(len(m[0])):
        col += 1
    return [lin, col]
	if m == []:
        return True