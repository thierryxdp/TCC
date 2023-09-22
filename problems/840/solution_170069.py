def bolos (A,B,C):
    ''' determina a quantidade de bolos que joão consegue fazer
    	int, int, int, --> int '''
    if (A//2) > (B//3) > (C//5):
        return (A//2)
    elif (A//2) < (B//3) > (C//5):
        return (B//3)
    elif (A//2) < (B//3) < (C//5):
        return (C//5)