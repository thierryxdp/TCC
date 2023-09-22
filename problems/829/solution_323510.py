def soma_h(n):
    ''' Retorna o resultado da equação H = 1 + 1/n
    int -> int'''
    
    resultado_h = 0
    for i in range(1, n+1):
        resultado_h += (1/i)
        
	return round(resultado_h, 2)