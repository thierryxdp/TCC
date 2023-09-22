def bolos(A, B, C):
    '''
    funcao que calcula quantos bolos joao consegue fazer, dadas
as quantidades de farinha, ovos e leite
'''
    return min(A//2,B//3,C//5)