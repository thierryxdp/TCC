def bolos(a,b,c):
    ''' dadas as variantes, ele calcula e retorna o numero maximo de bolos que joao pode fazer'''
    return min((a//2,b//3,c//5))