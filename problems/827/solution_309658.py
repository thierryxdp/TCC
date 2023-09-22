def qtd_divisores(n):
    divisores=[]
    for i in range(1,n+1):
        if (n%i)==0:
            qtd_divisores.append([i])
	return len(qtd_divisores)