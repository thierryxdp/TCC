def bolos(A,B,c):
    '''Dadas as quantidades de cada ingrediente, retorna a quantidade de bolos que João consegue fazer'''
    return max(A//2,B//3,C//5)