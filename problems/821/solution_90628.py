def fatorial(n):

	i = 1
	if n <= 1:
		return 1
	
	while i < n: 
		n = n * i 
		i += 1

	return f