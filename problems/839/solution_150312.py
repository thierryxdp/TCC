def carros(x,y=5):
    """calcula e retorna o numero de carros necessários para a viagem, para x como numero de pessoas e y a capacidade do carro"""
    return x//y + round(x%y)