def qtd_divisores(number):
    divisores = number
    
    for divisor in range(1,number+1):
		if (number % divisor) != 0:
            divisores -= 1
	return divisores