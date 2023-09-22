def conta_numero(numerto,matriz):
    contador = 0
    n=0
	x = len(matriz)
	while n < x:
        
        contador = contador + list.count(matriz[n])
        n = n+1
    return contador