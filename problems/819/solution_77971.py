def filtraMultiplos(l,n):
    l1 = []
    contador = 0
    while contador <= len(l):
        if l[contador]%n == 0:
            l1.append(l[contador])
    contador = contador + 1
	return l1