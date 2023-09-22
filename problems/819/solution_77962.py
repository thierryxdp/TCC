def filtraMultiplos(numeros,n):
    w=0
    k=[]
    while w<len (numeros)-1:
        w=w+1
        if numeros[w]%n==0:
            list.append(k,numeros[w])
	return k