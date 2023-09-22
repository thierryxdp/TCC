def carros(pessoas,capacidade=5):

    '''calcula os carros necessarios na viagem, int, int=>int'''

    automoveis = math.ceil(pessoas / capacidade)

    return automoveis