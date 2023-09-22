import math

def carros(p,c=5):
    '''calcula o numero exato de carros necessarios para determinada quantidade de pessoas''''
    return math.ceil(p//c)