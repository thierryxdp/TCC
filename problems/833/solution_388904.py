def conta_numero(numero,matriz):
    X=0
    Y=0
    W=0
    while X<len(matriz):
        W=0
        while W<len(matriz[0]):
        	if numero==matriz[X][W]:
                Y=Y+1
            W=W+1
		X=X+1
	return Y