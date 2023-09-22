import math
def bolos (a, b, c):
    '''Calcula a quantidade máxima de bolos que João pode fazer com os 
    ingredientes disponíveis. Dados a, b e c como entrada'''
    return min(math.floor(a/2 + b/3 + c/5)//3)