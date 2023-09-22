def bolos(A,B,C):
    '''Calcula e retorna a quantidade de bolos capaz de se fazer dado o numero de xicaras de farinha(A), de ovos(B) e de colheres de sopa de leite(C).'''
    return min(A//2,B//3,C//5)