import math
def carros (pessoas,capacidade=5):

    '''calcula os carros necessarios na viagem, int, int=>int'''

    carros == math.ceil (pessoas / capacidade)
    return carros