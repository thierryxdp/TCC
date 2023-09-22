def bolos(a,b,c):
    '''calcular quantidade de bolos possiveis a partir dos ingredientes disponíveis'''
    return round(min(a/2,b/3,c/5))