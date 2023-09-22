def carros(p,v):
    ''' funcao para calcular o numero exato de carros para levar as pessoas '''
    x = float(p) / float(v)
    return math.ceil(x)