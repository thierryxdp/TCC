def soma_h(n):
    
    resultado_h = 0
    for i in range(1, n):
        resultado_h += (1/resultado_h)
        
	return round(resultado_h, 2)