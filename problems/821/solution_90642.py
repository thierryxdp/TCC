def fatorial(n):
	""" Calcula o fatorial de um numero
	int -> int """
	i = 1
	if n <= 1:
		return 1
	
	while i < n: 
		i += 1
		n = n * i 
		

	return n