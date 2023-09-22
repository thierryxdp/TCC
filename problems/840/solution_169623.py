def bolos (a=2, b=3, c=5):
    '''Quantidade de bolos que Joao consegue fazer'''
    import math
    
    if a > 2 and b > 3 and c > 5:
        return math.ceil(0)
    if a <= 2 and a > 1 and b <= 3 and b > 1 and c <= 5 and c > 1 :
        return math.ceil(1)
    if 2*(a, b, c):
        return math.ceil(1)*2
    if 3*(a, b, c):
        return math.ceil(1)*3