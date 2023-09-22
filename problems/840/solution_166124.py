def bolos(A,B,C):
    '''Determina a maxima quantidade de bolos possiveis de serem feitos a partir de A xicaras de farinha, B ovos e C colheres de sopa de leite'''
    return min(A//2,B//3,C//5)