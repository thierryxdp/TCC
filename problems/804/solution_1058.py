def filtra_pares(x,y,z,w):
	filt = [x,y,z,w]
	tup = []
	for k in filt:
		if k%2 == 0:
			tup.append(k)
	return tup