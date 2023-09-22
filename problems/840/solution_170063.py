def bolos (A,B,C):
    ''' determina a quantidade de bolos que joão consegue fazer
    	int, int, int, --> int '''
    if A < B < C:
        return (A//2)
    elif A<B>C:
        return (B//3)
    else:
        return (C//5)