def carros(pessoas,capacidade=5):
    '''calcula o número de carros necessários para a viagem'''
    if pessoas%capacidade == 0:
        carros = pessoas//capacidade
    else:
        carros = pessoas//capacidade + 1
    return carros