import math
def bolos(A,B,C):
    '''calcula o maximo de numero de bolos feitos com A
    xicaras de farinha de trigo, B ovos e C colheres de 
    sopa de leite'''
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))