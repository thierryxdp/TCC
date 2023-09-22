def soma_h(n):
    s=0
    k = 1
    for numero in range(1, n):
        k = 1/numero
        s += k
	return round(s,2)