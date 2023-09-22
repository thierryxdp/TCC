def media(matriz):
    X=0
    Z=0
    W=0
    while X<len(matriz):
        Y=0
        while Y<len(matriz[0]):
            Z=Z+matriz[X][Y]
			Y=Y+1
        	W=W+1
		X=X+1
    return round(Z/W,2)