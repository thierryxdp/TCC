import math
def bolos(A,B,C):
    '''calcula a quantidade máxima de bolos que podem ser feitos com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite'''
    return min(A//2,B//3,C//5)