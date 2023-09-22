import math
def carros(pessoas,convencional=5):
    '''calcula a quantidade de carros necessária para transportar uma quantidade de pessoas'''
    return (math.ceil((pessoas/convencional)))