import math
def carros(p:'int',c:'int'=5)->'int':
    '''calcula a quantidade c de carros necessarios para uma viagem com quantidade p de pessoas'''
    return math.ceil(p/c)