def filtraMultiplos(lista,n):
    y=[]
	for x in lista:
        if x%n==0:
            y.append(x)
    return y