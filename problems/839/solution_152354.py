def carros (n, c=5):
    """calcular o número de carros necessarios dado o número de
    passageiros n e a capacidade c de cada carro"""
    return math.ceil (n/c)