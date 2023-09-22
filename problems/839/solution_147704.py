def carros(p,cv=5)
    """Número de carros necessários para viagem. p(passageiros) cv(capacidade do carro)"""
    return math.ceil(p/cv)