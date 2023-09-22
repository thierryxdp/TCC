def carros(pessoas,acentos5):
    '''calcula o valor exato de carros necessários para uma viagem'''
    import math
    carros = math.ceil(pessoas/acentos)
    return carros