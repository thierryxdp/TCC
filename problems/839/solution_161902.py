import math
def carros(num_pessoas,car=5):
    ''' int --> int '''
    x = num_pessoas/car
    return math.ceil(x)