def soma_h(N):
	H=0
	for n in range(1,N+1):
        H+=round(n**(-1),2)
    return H