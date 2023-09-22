def bolos(A,B,C):
    ''' Calcula e retorna a quantidade máxima de bolos inteiros que joão pode fazer'''
    return min(A//2,B//3,C//5)