def soma_h(N):
	# H = 1 + 1/2 + 1/3 ... + 1/N
	H = 0
	for n in range(1, N+1):
		H += 1/n
	return round(H, 2)