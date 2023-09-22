def qtd_divisores(n):
    divisores = 1
    for i in range(2,n):
        if n % i == 0:
            divisores += 1
            
	return divisores