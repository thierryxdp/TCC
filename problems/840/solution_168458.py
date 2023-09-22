#Questao 3
def bolos1(A, B, C):
    '''
Funcao que determina qual a quantidade maxima de bolos que Joao consegue fazer.
Sendo A=xicaras de farinha de trigo, B=ovos e C=colheres de sopa de leite.
    '''
    A=(a//2)
    B=(b//3)
    C=(c//5)
    return min(A, B, C)