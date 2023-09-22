def carros(pessoas,veiculos=5):
    """Calcula o número exato de carros necessários para a viagem"""
    return float(int(pessoas // veiculos+0.7))