def bolos(A,B,C):
    '''Função que calcula a quantidade de bolos que consegue fazer com A: xícaras de trigo, B: ovos, C: colheres de leite
    int, int, int -> int'''
    return min(A//2, B//3, C//5)