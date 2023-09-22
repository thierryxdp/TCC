from math import ceil 
def carros(pessoas,capacidade=5):
    '''calcula e retorna o numero de carros necessarios para transportar um grupo de pessoas'''
    return ceil(pessoas/capacidade)