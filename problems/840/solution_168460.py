#Questao 3
def bolos(A, B, C):
    '''
Funcao que determina qual a quantidade maxima de bolos que Joao consegue fazer.
Sendo A=xicaras de farinha de trigo, B=ovos e C=colheres de sopa de leite.
    '''
    A=(A//2)
    B=(B//3)
    C=(C//5)
    return min(A, B, C)