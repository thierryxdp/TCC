def bolos(A,B,C):
    '''Esta função determina a quantidade máxima de bolos
    que se consegue fazer, dadas as quantidades de A, B e
    C, com entradas de três números inteiros,
    quantidade necessária para um bolo:
    2 xícaras de farinha de trigo = A
    3 ovos = B
    5 colheres de sop de leite = C'''
    return math.min(A//2,B//2,C//2)