def filtraMultiplos(numeros,n):
    w=0
    k=[]
    while w>len (numeros):
        if numeros[w]%n==0:
            k+numeros[w]
	return k