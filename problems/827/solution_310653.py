def qtd_divisores(n):
	
	d = 2

	i = 2
	while i<n:
		d += 1 if n%i == 0 else 0
		i += 1

	return d