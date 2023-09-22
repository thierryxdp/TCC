from math import min
def bolos(a,b,c):
    '''calcula a quantidade máxima de bolos que podem ser feitos a partir dos igredientes a (xícaras de farinha de trigo), b (número de ovos) e c (número de colheres de sopa de leite)'''
    return min(a//2,b//3,c//5)