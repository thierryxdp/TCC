def soma_h(n):
	h = 0
	if n == 0:
		return 0
	else:
		for i in range(1,n+1):
			h += 1/i
		return round(h,2)