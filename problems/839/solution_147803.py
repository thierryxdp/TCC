def carros (pessoas, capacidade):
    """Calcula e retorna o número exato de carros necessário para uma viagem de até 50 pessoas"""
    if (not num % 5):
        return pessoas/capacidade
    else:
        (pessoas//capacidade)+1