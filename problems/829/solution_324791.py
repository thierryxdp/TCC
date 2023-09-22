def soma_h(n):
	total = 0
	for x in range(1,n+1):
		total = total + 1/x
	return round(total,2)