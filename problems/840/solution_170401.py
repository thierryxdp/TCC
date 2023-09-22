def bolos(a,b,c):
    '''
    função que calcula quantos bolos joao e capaz de fazer com determinadas 
    quantidades de material. Assuma a como xicaras de farinha, b como ovos e c como colheres
    de leite
    int, int,int -> int
    '''
    if ((a/2) < (b/3)) and ((a/2) < (c/5)):
    	return (a/2)
    elif ((b/3) < (a/2)) and ((b/3) < (c/5)):
    	return (b/3)
    else:
        return (c/5)