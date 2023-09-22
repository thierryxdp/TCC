def fatorial(num):
    '''
    	Função que dado um número calcula seu fatorial.
        int -> int
	'''
    n=1
    while num>=1:
        n=n*num
        n=n-1
    return n