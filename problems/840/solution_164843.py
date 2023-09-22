import math
def bolos(a,b,c):
    '''calcula a quantidade de bolo que podem ser feitos com a quantidade de cada ingrediente. 
    A farinha, os ovos e as colheres de sopa de leite são inteiros'''
  
    return math.floor(min(a/2,b/3,c/3))