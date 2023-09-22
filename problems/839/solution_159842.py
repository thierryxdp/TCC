def carros(n_pessoas,cap_carro=5):
    '''calcula e retorna o numero exato de carros necessários para  
    transportar n_pessoas, dada a capacidade de cada carro cap_carro;
    float, float -> int'''
    import math
    return math.ceil(n_pessoas/cap_carro)