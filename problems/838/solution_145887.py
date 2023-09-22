def num_bombons(d,p):
    '''Retorna o numero de bombons que pedrinho pode comprar
    dado seu dinheiro(d) e preço(p) dos bombons
    float,float->float'''
    import math
    return math.floor(d/p)