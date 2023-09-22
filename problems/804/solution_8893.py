def filtra_pares(t):
	n = []
	for i in range(0, len(t)):
		if t[i]%2==0:
			n.append(t[i])
	return n