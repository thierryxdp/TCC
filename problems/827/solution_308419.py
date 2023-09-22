def qtd_divisores(n):
	divisores=1
    i=1
	while i < n/2:
    	if n%i == 0:
        	divisores = divisores + 1
        i = i + 1
    return divisores