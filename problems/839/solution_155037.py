def carros(pessoas,carros,van):
    '''calcular quantos carros precisa na viagem'''
    if pessoas>5:
        return str(carros)
    elif pessoas<=5:
        return str(van)