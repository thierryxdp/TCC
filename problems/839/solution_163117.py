def carros(pessoas, capacidade=5):
    """essa função me retornará a quantidade de carros convencionais necessários"""
    automoveis= math.ceil(pessoas/capacidade)
    return automoveis