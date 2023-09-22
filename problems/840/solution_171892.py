def bolos(A,B,C):
    '''retorna a quantidade maxima de bolos que da pra preparar'''
    A=(A//2)
    B=(B//3)
    C=(C//5)
    return min(A,B,C)