def eh_quadrada(matriz):
    d1=0
    d2=0
	for i in range(len(matriz)):
        d1=d1+1
    	for x in range(len(matriz[i])):
        	d2=d2+1
    if d1==d2*i:
        return True
    else:
        return False