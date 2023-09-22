def bolos(A,B,C):
    '''Calcula a quantidadade maxima de bolos que Joao consegue fazer, dados as quantidades de farinh de trigo A, ovo B e leite C'''
    b=min(A//2,B//3,C//5)
    return b