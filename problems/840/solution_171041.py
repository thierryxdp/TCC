import math
def bolos(far, ovo, leite):
    '''função que define a quantidade de bolos que podem ser feitos com medidas exatas, de acordo com a quantidade de ingredientes. int, int, int --> int.'''
    return math.floor(min((far/2), (ovo/3), (leite/5)))