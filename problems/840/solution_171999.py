def bolos(a,b,c):
    """Função que determina a quantidade máxima de bolos que João consegue fazer, dados A, B e C;
    int, int, int -> int"""
    f=(a//2)
    o=(b//3)
    l=(c//5)
	if (f<o) and (f<l):
    	return f
	elif (o<f) and (o<l):
    	return o
	else:
    	return l