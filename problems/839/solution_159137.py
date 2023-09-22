def carros(pessoas, capacidade=5):
    '''calcula a quantidade de carros necessario dado o n° de pessoas'''
    import math
    return math.ceil(pessoas/capacidade)