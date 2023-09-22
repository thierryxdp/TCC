def qtd_divisores(n):
	d=0
	for i in range(-99,999):
		if n%i == 0:
			d += 1
		else:
			pass
	return d