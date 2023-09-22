def bolos(a,b,c):
    '''Entre com oa valores para o numero de xicarasde farinha (a), ovos(b) e
    colher de sopa (c) respectivamente para obter a quantidade maxima de bolos
    que podem ser feitos'''
    x = min((a//2),(b//3),(c//5))
    return x