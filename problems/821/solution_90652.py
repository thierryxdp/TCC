def fatorial(n):
	""" Calcula o fatorial de um numero
	int -> int """
	i = 1
	f = n
	if n <= 1:
		return 1
	
	while i < n: 
		i += 1
		f = f * i
		

	return f