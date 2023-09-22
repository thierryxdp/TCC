import math
def carros(p,c=5):
    '''calcula e retorna o numero de carros exatos necessarios para uma viagem'''
    return math.ceil (p//c)