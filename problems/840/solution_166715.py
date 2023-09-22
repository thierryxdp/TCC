import math
def bolos(a,b,c):
    '''calcula a quantidade de bolos dados o numero de ingredientes a, b e c'''
    return min((a/2)+(b/3)+(c/5))