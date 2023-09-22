def bolos (a=2, b=3, c=5):
    '''Quantidade de bolos que Joao consegue fazer'''
    import math
    if a <= 1 or b <= 2 or c <= 5:
        return (0)
    if (a == 2, b == 3, c == 5):
        return (2)
    if a * 2 and b * 2 and c * 2:
        return (2)
    if a * 3 and b * 3 and c * 3:
        return (3)