def carros(p, c=5):
    ''' funcao para calcular o numero exato de carros para levar as pessoas '''
    veiculos= math.ceil(p / c)
    return veiculos