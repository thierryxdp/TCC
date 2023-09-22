def eh_quadrada(matriz):
    d1=0
    d2=0
	for i in range(len(matriz)):
        d1=d1+1
    	for x in range(len(matriz[i])):
        	d2=d2+1
    if d1>7 and d2>7:
        return True
    else:
        return False