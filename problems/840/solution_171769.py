import math
def bolos(a,b,c):
    '''
    
    '''
    if a < 2 or b <3 or c<5:
        return 0
    else:
        return math.min(a/2, b/3, c/5)