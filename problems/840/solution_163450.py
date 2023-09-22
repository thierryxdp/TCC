def bolos(A,B,C):
    '''Calcula quantos bolos é possível ser feito'''
    if A<2:
        return 'falta ingrediente'
    elif B<3:
        return 'falta ingrediente'
    elif C<5:
        return 'falta ingrediente'
    else:
        return (A+B+C)//10