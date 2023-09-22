def fatorial(n):
    '''função que retorna o fatoraial de um numero'''
    '''int -> int'''
    prox = 1
    k = n
    while prox < n:
        k = k *(n-prox)
        prox += 1
	return k