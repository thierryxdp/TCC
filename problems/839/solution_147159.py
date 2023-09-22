import math
def carros(x,c=5):
    '''calcula o número de carros necessários para a viagem considerando a capacidade de 5 pessoas. capacidades diferentes devem ser fornecidas'''
    return math.ceil(x/c)