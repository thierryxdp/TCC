def qtd_divisores(n):
	mult=0
    for count in range(1,n+1):
        if (n % count == 0):
        mult += 1
    return mult