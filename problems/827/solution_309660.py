def qtd_divisores(numero):
	'''
    	funcao que conta a quantidade de divisores que um numero tem
        int -> int
    '''
    divisores = 0
    for x in range(numero+1):
        if numero%x = 0:
            divisores += 1
    return divisores