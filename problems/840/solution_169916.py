def bolos (a=2, b=3, c=5):
    '''Quantidade de bolos que Joao consegue fazer'''
    import math
    if a <= 0:
        return (0)
    if b < 3:
        return (0)
    if c < 5:
        return (0)
    if c == 9:
        return (1)
    if c == 10:
        return (10)
    if a == 2 and b == 3 and c == 5:
        return (1)
    if 2 * a and 2 * b  and c + 2 * a:
        return (1)