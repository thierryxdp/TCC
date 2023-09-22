def filtra_pares(x,y,z,w):
	n1 = x%2
    n2 = y%2
    n3 = z%2
    n4 = w%2

    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        return (x,y,z,w)