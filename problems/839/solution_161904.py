def carros (pessoas, capacidade=5):
    """calcula o número extao de carros necessários para uma viagem. int, int-> int"""
    return math.ceil(pessoas/capacidade)