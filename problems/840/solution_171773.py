import math
def bolos(a,b,c):
    '''
    
    '''
    if a < 2 or b <3 or c<5:
        return 0
    else:
        if a/2 < b/3 and c/5:
            return a//2
        if b/3 < a/2 and c/5:
            return b//3 
        if c/5 < a/2 and b/3:
            return c//5