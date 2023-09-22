import math
def carros(p,c=5):
    '''calcula e retorna o número nescessário de carros para uma viagem dado o número de pessoas p e a capacidade c do veículo; int, int -> int'''
    return math.ceil(p/c)