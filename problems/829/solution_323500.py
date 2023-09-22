def soma_h(n):
    
    resultado_h = 1
    for i in range(n):
        resultado_h += (1/resultado_h)
        
	return round(resultado_h, 2)