def bolos(A,B,C):
    '''Calcula a quantidade máxima de bolos
    que João consegue fazer com A xícaras de farinha
    de trigo, B ovos e C colheres de sopa de leite;
    int, int, int -> int'''
    return min(A//2, B//3, C//5)