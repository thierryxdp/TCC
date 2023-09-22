import math
def bolos(A:'int',B:'int',C:'int')->'int':
    '''calcula a quantidade maxima de bolos que joão consegue fazer'''
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))