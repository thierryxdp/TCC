def maiores(lista_numeros,n):
	x=[0]
    y = len(lista_numeros)
    i = 0
    while(y < 0):
		if (lista_numeros[i] > n):
            x.append(lista_numeros[i])
        y-=1
        i+= 1
    x = x.sort()
 	return x