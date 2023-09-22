import math
def carros (num_pessoas, capacidade=5):
    '''calcula a quantidade de carros necessários para transportar num_pessoas, 
    dado também a capacidade do veículo int, int => int'''
    #quantos carros são necessários?
    
    return math.ceil (num_pessoas / capacidade)