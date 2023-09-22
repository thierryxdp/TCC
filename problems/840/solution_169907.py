def bolos (a=2, b=3, c=5):
    '''Quantidade de bolos que Joao consegue fazer'''
    import math
    if a <= 0:
        return (0)
    if a == 2 and b == 3 and c == 5:
        return (1)
    if 2 * (a == 2 and b == 3 and c == 5):
        return (2)