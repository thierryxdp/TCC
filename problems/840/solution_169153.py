import math
def bolos(A , B , C):
    '''esta funcao serve para indicar a quantidade de bolos que joao consegue fzr com os ingredientes em casa.'''
    return math.ceil(A//2 , B//3 , C//5)