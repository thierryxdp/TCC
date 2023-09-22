def bolos (A,B,C):
    ''' determina a quantidade de bolos que joão consegue fazer
    	int, int, int, --> int '''
    if A > 2 and B > 3 and C > 5 and A<B<C:
        return (A//2)
    elif A> 2 and B > 3 and C > 5 and A<B>C:
        return (B//3)
    elif A > 2 and B > 3 and C > 5 and C>A<B:
        else:
            return 0