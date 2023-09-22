def carros (pessoas, capacidade=5):
    """Calcula e retorna o número exato de carros necessários para uma viagem"""
    if (pessoas%capacidade==0):
        return pessoas//capacidade
    else:
        return (pessoas//capacidade)+1