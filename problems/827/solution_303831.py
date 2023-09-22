def qtd_divisores(number):
    divisores = number
    
    for divisor in range(1,number+1):
        if (number >= 0):
            if (number % divisor) != 0:
                divisores -= 1
        else:
            return 0
	return divisores