def bolos(A,B,C):
    '''retorna a quantidade de bolos possiveis de se fazer
    A = xicaras de farinha 
    B = ovos 
    C = colheres de sopa de leite'''
    return min(A//2,B//3,C//5)