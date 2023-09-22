def bolos(A,B,C)
	'''
    Funçao que calcula o numero de bolos que consegue fazer em relaçao 
    ao numero de ingredientes A,B e C disponiveis
    int, int, int -> int
    '''
    a=A//2
    b=B//3
    c=C//5
    return min(A,B,C)