import math
def carros(pessoas,capacidade=5):
    '''calcula o numero de carros necessario para realizar uma viagem, dadas a quantidade de pessoas e a capacidade do carro caso esta seja diferente de 5
    int,int->int'''
    return math.ceil(pessoas/capacidade)