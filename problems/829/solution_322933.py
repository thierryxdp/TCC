def soma_h(n): 
	divisor = 1
    calculo = 1
    for divisor in range(2,n+1):
        calculo=calculo+(1/divisor)
    return calculo