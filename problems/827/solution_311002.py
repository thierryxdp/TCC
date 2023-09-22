def qtd_divisores(num):
    a = 1
	while a <= num:
    	x = num % a
    	a = a +1
    if x == 0:
        return (a-1)