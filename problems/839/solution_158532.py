import math
def carros(n_pessoas, capacidade_veiculos=5):
    '''calcula e retorna o numero de carros necessarios para transportar n_pessoas dependendo da capacidade_veiculos'''
    return math.ceil(n_pessoas/capacidade_veiculos)