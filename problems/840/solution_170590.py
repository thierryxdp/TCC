import math
def bolos(a,b,c):
    '''Retorna a quantidade máximade bolos que João consiguirá fazer de acordo com os ingredientes disponiveis'''
    bolos = min (2,3,5)
    
    return math.floor(min(a,b,c))