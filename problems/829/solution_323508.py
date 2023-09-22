def soma_h(n):
    
    resultado_h = 1
    for i in range(1, n+1):
        resultado_h += (1/i)
        
	return round(resultado_h, 2)