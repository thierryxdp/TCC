def qtd_divisores(x):
    divisores = 0
    for divisor in list(range(1, x+1)):
        if x%divisor==0:
            divisores += 1
	return divisores