def soma_h(numero):
    H = 0
    for contador in range(1,numero+1):
		H = H + round(1/contador, 2)
	return H