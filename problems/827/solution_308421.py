def qtd_divisores(n):
	divisores=1
    i=1
	if n>0:
        while i < n//2 + 1:
    		if n%i == 0:
        		divisores = divisores + 1
        	i = i + 1
		return divisores
    return 0