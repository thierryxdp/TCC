def bolos(A,B,C):
    '''Calcula quantos bolos é possível ser feito'''
    if A<2:
        return 0
    elif B<3:
        return 0
    elif C<5:
        return 0
    else:
        return (A+B+C)//10