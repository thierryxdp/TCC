def maiores(lista_numeros,n):
	x=[]
    n = len(lista_numeros)
    i = 0
    while(n < 0):
		if (lista_numeros[i] > n):
            x.append(lista_numeros[i])
        n-=1
        i+= 1
 	return x.sort()