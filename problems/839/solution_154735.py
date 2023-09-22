def carros(pessoas, capacidade=5):
    """calcula e retorna o número de carros para a viagem"""
    automoveis=math.ceil(pessoas/capacidade)
    return automoveis