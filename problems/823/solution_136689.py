def faltante(L):
    n = int(len(L)) + 1
    i = 1
    while i<= n:
        if i in L:
            i = i + 1
        else:
			return i