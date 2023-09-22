def bolos (a=2, b=3, c=5):
    '''Quantidade de bolos que Joao consegue fazer'''
    import math
    if a < 2:
        return (0)
    if b < 3:
        return (0)
    if c < 5 :
        return (0)
    if c > 15 and c < 50:
        return 
    if (a == 2 and b == 3 and c == 5):
        return (1)
    if (a * 2) + (c * 2) <= b:
        return (0)
    if (a * 3) * (b * 3) <= c :
        return (3)
    if (a + b) == c:
        return (3)
    if (a*5, b*5, c*100):
        return (5)