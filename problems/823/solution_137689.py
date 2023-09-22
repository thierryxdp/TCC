def faltante(L):
    d = {}
    for i in range(1,len(L)+2):
        d[i] = 0
	for i in L:
        del d[i]
	return list(d.keys())[0]