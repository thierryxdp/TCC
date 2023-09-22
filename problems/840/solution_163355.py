def bolos(A,B,C):
    '''função que calcula a quantidade de bolos que João conseguirá fazer com A xícaras de farinha, B ovos e C colheres de sopa de leite.
    int, int, int --> int'''
    return min(round(A/2-0.5),round(B/3-0.5),round(C/5-0.5))