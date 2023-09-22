def bolos(A,B,C):
    '''Calcular a quantidade de bolos que podem ser feitas, favor entrar com números int'''
    A= A//2
    B= B//3
    C= C//5
    if A<=B and A <=C:
        return A
    elif B <=A and B <=C:
        return B
    elif C <=A and C <=B:
        return C