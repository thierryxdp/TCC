def carros(p,c=5):
    ''' função que calcula o número exato de carros para uma viagem dado o número de pessoas(int)'''
    import math
    return math.ceil(p/c)