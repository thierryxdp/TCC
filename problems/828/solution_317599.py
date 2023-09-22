def qtd_divisores(n):
	'''
    	funcao que verifica se um numero e primo ou nao. Caso esse 
        numero seja primo, a funcao retorna True , se ele nao for, a 
        funcao retorn False.
        int -> int
    '''
    divisores = 0
    for x in range(1,n+1):
        if n % x == 0 :
            divisores += 1
    if divisores > 2:
        return False
    if divisores = 2:
        return True
    if divisores = 1:
        return False