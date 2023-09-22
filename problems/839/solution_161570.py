def automoveis (pessoas,capacidade=5):

    '''calcula os automoveis necessarios na viagem, int, int=>int'''

    automoveis == math.ceil (pessoas / capacidade)
    return automoveis