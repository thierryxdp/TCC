import math
def bolos(A,B,C):
    '''calcula o número máximo de bolos que é possível fazer com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite; int, int -> int'''
    return math.floor(min((A/2),(B/3),(C/5)))