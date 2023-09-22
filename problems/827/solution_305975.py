def qtd_divisores(n):
    r = 0
    for i in range(1, n+1):
        if n%i == 0:
            r = r+1
	return r