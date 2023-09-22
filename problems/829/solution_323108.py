def soma_h(numero):
    H = 0
    for contador in range(1,numero+1):
		H = H + 1/contador
	return round(H, 2)