def bolos(A,B,C):
    '''funcao que retorna a quantidade maxima de bolos que se pode fazer dados tres igredientes'''
    return min(A//2,B//3,C//5)