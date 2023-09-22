def carros(pessoas):
    '''calcular quantos carros precisa na viagem'''
    if pessoas>5:
        return str(carrosNaoConvencionais)
    elif pessoas<=5:
        return str(carrosConvencionais)