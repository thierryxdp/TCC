def carros (pessoas, capacidade=5):
    """função que retorna o numero exato de carros necessários para uma viagem, dados o numero de pessoas e a capacidade de carro"""
    return int (pessoas+2//capacidade)