def carros (pessoas, capacidade=5):
    """Calcula e retorna o número exato de carros necessário para uma viagem de até 50 pessoas"""
    return (pessoas//capacidade)+1