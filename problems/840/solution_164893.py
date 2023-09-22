import math
def bolos(a,b,c):
    '''calcula a quantidade de bolo que podem ser feitos com a quantidade de cada ingrediente. Sendo 
    "a" a farinha, "b" os ovos e "c" as colheres de sopa de leite, todas as entradas sendo um float'''
    return math.floor(min(a/2,b/3,c/5))