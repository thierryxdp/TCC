import math
def bolos(a,b,c):
    '''calcula a quantidade de bolos dados o numero de ingredientes a, b e c'''
    return min(a/2)+min(b/3)+min(c/5)