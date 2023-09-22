def carros(p,c=5):
    """Função que calcula o número de carros necessários para uma viagem, dado o número de pessoas e a capacidade dos veículos, caso não convencionais"""
    return math.ceil(p/c)