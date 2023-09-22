def soma_h(x):
    H = 0
    for valor in list(range(1,x+1)):
        H = H + 1/valor
	return round(H, 2)