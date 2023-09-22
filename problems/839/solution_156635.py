def(passageiros,capacidade_carro=5):
    '''
    A funcao deve dividir o numero de pesssoas pela 
    capacidade do carro
    '''
    automoveis = math.ceil(pessoas/capacidade)
    return(automoveis)