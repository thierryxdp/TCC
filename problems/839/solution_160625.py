import math
def carros(p,c=5):
    '''calcula o número exato de carros necessários para esta viagem;
    int,int -> int'''
    return math.ceil(p/c)