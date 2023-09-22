def carros (pessoas, capacidade=5):
    """Calcula e retorna o número exato de carros necessário para uma viagem de até 50 pessoas"""
    if pessoas%capacidade=0:
        return pessoas//capacidade
    else:
        (pessoas//capacidade)+1