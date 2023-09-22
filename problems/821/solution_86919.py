def fatorial(n):
    '''função que retorna o fatoraial de um numero'''
    '''int -> int'''
    prox = 1
    while prox < n:
        n = n *(n-prox)
        prox += 1
	return n