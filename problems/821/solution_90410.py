def fatorial(n:int)->int:
    '''recebe um número e retorna seu fatorial'''
    i= n-1
    while i > 0:
        n *= i
        i -= 1
	return n