def qtd_divisores(n):
    divisores = []
	for c in range(0,n+1):
    	if n%c == 0:
        	divisores.append(c)
    return len(divisores)