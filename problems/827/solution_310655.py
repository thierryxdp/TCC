def qtd_divisores(n):
	
	# machine teaching diz que inteiros
	# não positivos não possuem divisores :0
	if n <= 0:
		return 0

	d = 2

	i = 2
	while i<n:
		d += 1 if n%i == 0 else 0
		i += 1

	return d