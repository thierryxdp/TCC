import math
def bolos(a,b,c):
    '''calcula a quantidade de bolos dados o numero de ingredientes a, b e c'''
    return math.isqrt(a+b+c)//10