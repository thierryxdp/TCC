def bolos (a=2, b=3, c=5):
    '''Quantidade de bolos que Joao consegue fazer'''
    import math
    return math.ceil(max(a, b, c))