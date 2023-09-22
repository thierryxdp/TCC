def bolos(A,B,C):
    '''Calcule e retorne a quantidade máxima que joão consegue fazer. Considere como entradas os números inteiros A,B,C, indicando respectivamente o número de xícaras de farinha de trigo, o número de ovos eo número de colheres de sopa de leite'''
    A1=A/2
    B1=B/3
    C1=C/5
    return int((min(A1+B1+C1))