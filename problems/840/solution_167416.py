import math
def bolos (a: int,b: int,c: int) -> int:
    '''calcula e retorna o a quantidade máxima de bolos;a<2=0,b<3=0,c<5=0 ; int,tint -> int'''
    return math.floor ((a//2)+(b//3)+(c//5)//3)