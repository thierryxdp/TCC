import math

def bolos(a,b,c):
    '''calcula a quantidade de bolos que podem ser feitos com a 
    quantidade de cada ingrediente inserida. a xícaras de farinha 
    de trigo, b ovos e c colheres de sopa de leite, 
    os valores inseridos devem ser do tipo float'''
    return math.floor(min(a/2,b/3,c/5))