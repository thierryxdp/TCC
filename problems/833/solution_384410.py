def conta_numero(numero,matriz):
    '''Conta quantas vezes um numero aparece em uma dada matriz.
    int, list -> int'''
	x=numero
	y=matriz
    a=0
    for i in range(len(y)):
        for j in range(len(y[i])):
        	if x==y[i][j]:
            	a+=1
    return a