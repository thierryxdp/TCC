import math
def carros(x, y=5):
    '''int, int -> float'''
    num_carros = x/y
    return math.ceil(num_carros)