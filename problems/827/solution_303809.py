def qtd_divisores(number):
    for i in range(1,number+1):
		if (number % i) == 0:
            soma += 1
			return soma