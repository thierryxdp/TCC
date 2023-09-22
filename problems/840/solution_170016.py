def bolos(A,B,C):
    '''Esta função determina a quantidade máxima de bolos
    que se consegue fazer, dados as quantidades de A, B e C,
    com entradas de três números inteiros, quantidade 
    necessária para um bolo:
    2 xícaras de farinha de trigo = A
    3 ovos = B
    5 colheresde sopa de leite = C'''
    return min(A//2,B//3,C//5)