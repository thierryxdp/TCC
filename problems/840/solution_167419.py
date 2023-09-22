import math
def bolos (a: int,b: int,c: int) -> int:
    '''calcula e retorna o a quantidade máxima de bolos; int,tint -> int'''
    return math.ceil((a+b+c)//10)