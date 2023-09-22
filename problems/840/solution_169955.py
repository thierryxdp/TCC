def bolos(a,b,c):
    '''função que calcula a quantidade de bolos que João pode fazer, dado os ingredientes x
    farinha, b ovos e c leites.'''
     return min(a//2, b//3, c//5)