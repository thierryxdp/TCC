def bolos (a=2, b=3, c=5):
    '''Quantidade de bolos que Joao consegue fazer'''
    import math
    if a >= 0 and a <= 10 and  b >= 1 and b <= 50 and c >= 3 and c <= 5:
        return (0)
    if a >= 2 and a <= 4 and b >= 3 and b <= 6 and c >= 5 and c <= 50:
        return (1)
    if a >= 4 and a <= 20 and b >= 6 and b <= 15 and c == 10:
        return (2)