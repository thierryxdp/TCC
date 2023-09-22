def qtd_divisores(number):
    divisores = 0
    for i in range(1,number+1):
		if (number % i) == 0:
            divisores += 1
	return divisores