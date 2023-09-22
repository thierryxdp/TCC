def bolos(A,B,C):
    '''A numero de xicara de farinha de trigo, B o numero de ovos
    e C o numero de colheres de sopa de leite que joao tem em casa
    com isso temos a funcao que determina qual a quantidade maxima
    de bolos que ele consegue fazer
    int,int,int->int'''
    return min(A//2,B//3,C//5)