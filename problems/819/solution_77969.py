def filtraMultiplos(l,n):
    l1 = []
    contador = 0
    while contador <= len(l):
        if l[contador]%8 == 0:
            l1.append(l[contador])
	return l1