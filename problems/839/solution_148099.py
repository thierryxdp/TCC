def carros(npessoas,viagem=5):
    '''Calcula a quantidade de carros necessários para a viagem'''
    import math
    return math.ceil(npessoas/viagem)