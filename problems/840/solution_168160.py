def bolos(a, b, c):
    '''Retorna a quantidade de bolos podem ser feitas de acordo com o número de ingredientes.
    int, int, int -> int'''
	return min(a // 2, b // 3, c // 5)