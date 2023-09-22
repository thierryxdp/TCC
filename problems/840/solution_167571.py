import math
def bolos (a: int,b: int,c: int) -> int:
    '''calcula e retorna o a quantidade máxima de bolos; int,int -> int'''
    return min (a//2,b//3,c//5)