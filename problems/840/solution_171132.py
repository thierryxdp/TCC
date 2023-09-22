import math
def bolos(A,B,C):
    '''calcula e retorna o número de bolos que consegue fazer; int,int,int->int'''
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))