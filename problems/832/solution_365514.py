def eh_quadrada(matriz):
    n1 = 0
    n2 = 0
    for i in matriz:
        n1+=1
        for j in i:
            n2+=1
    if n1 != 0:
    	if n1 == n2/n1:
        	return True
    	else:
        	return False
    else:
        return True