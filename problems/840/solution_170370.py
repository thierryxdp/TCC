def bolos (A, B, C):
    '''Função que calcula numero possível de bolos; int,int,int -> int'''
    return min((A//2),(B//3),(C//5))