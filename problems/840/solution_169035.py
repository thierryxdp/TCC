def bolos(A,B,C):
    '''
    funcao que retorna a quantidade minima de
    bolos, dadas as quantidades de igredientes
    A,B e C
    int,int->int
    '''
    bolo=(A//2,B//3,C//5)
    return min(bolo)