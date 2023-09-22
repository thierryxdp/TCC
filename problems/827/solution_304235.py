def qtd_divisores(n):
    if n < 0:
        return 0
    
    divisores = 2
    for i in range(2,n):
        if n % i == 0:
            divisores += 1
            
	return divisores