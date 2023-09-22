def carros(pessoas,capacidade=5):
    """calcula a quantidade de carros necessaria para transportar o numero de passageiros fornecido"""
    return int((pessoas/capacidade)+0.5)