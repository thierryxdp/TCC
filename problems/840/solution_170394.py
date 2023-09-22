def bolos(a,b,c):
    '''
    função que calcula quantos bolos joao e capaz de fazer com determinadas 
    quantidades de material. Assuma a como xicaras de farinha, b como ovos e c como colheres
    de leite
    int, int,int -> int
    '''
	read (a)
    read (b)
    read (c)
    a==(a/2)
    b==(b/3)
    c==(c/5)
    if ((a) <= (b)) and ((a) <=(c)):
    	return (a)
    elif ((b) <= (a)) and ((b) <= (c)):
    	return (b)
    else:
        return (c)