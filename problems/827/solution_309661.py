def qtd_divisores(n):
	'''
    	funcao que conta a quantidade de divisores que um numero tem
        int -> int
    '''
    divisores = 0
    for x in range(n+1):
        if n % x = 0:
            divisores += 1
    return divisores