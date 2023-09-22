def bolos(A,B,C):
    ''' função que calcula a quantidade máxima de bolos que da para fazer com os ingredientes disponibilizados(A,B,C)'''
    a=A//2
    b=B//3
    c=C//5
    return min(a,b,c)