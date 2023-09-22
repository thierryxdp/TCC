def qnt_divisores(n):
    divisores = 0
    for i in range(0,n):
        if n%i==0:
            divisores +=1
	return divisores