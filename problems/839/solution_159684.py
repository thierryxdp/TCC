import math
def carros(p, v=5):
    '''função que retorna a quantidade necessária de carros para transportar um dado número p de pessoas e o número de vagas v caso seja diferente de 5'''
    return math.ceil(p / v)