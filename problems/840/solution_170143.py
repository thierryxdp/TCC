def bolos(A,B,C):
    '''Calcular a quantidade de bolos que podem ser feitos, favor entrar com números inteiros'''
    A= A//2
    B= B//3
    C= C//5
    if C<=A:
       return C
    elif C>A or C<=B:
       return C