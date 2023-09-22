def soma_h(n):
	total = 0
	x = 1
	while x <= n:
		total = total + 1/x
		x = x + 1
	return round(total, 2)