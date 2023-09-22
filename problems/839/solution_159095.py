def carros(pessoas,acentos=5):
    '''calcula o valor exato de carros necessários para uma viagem'''
    carros = math.ceil(pessoas/acentos)
    return carros