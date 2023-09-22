def bolos(a,b,c):
    '''calcula a quatidade de bolos que podem ser feitos'''
    import math
    A = (a/2)
    B = (b/3)
    C = (c/5)
    R = min(A,B,C)
    return math.floor(R)