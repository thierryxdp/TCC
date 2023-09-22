def bolos(A,B,C):
    '''retorna o número de bolos que ele irá fazer dado as xícaras de farinha(A), ovos(B) e colheres de sopa(C)'''
    return min((A//2),(B//3),(C//5))