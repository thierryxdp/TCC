import math
def carros(p,c=5):
    '''calcula e retorna o número de carros necessários para a viagem; int,int->int'''
    return math.ceil(p/c)