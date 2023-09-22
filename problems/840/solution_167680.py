def bolos(a,b,c):
    ''' funcao que calcula o maximo de bolos que ele consegue fazer'''
    x = float(a/2) + float(b/3) + float(c/5)
    return float(max(x))