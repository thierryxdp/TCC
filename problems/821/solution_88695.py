def fatorial(n):
    
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 'Não existe'
    else:
        resultado = n*fatorial(n-1)
    	return resultado