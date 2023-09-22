def carros(p,c=5):
    """retorna o número de carros necessários para a viagem, com base no número p de pessoas e na capacidade c do carro"""
    if p%c == 0:
        r=0
    else: r=1
    return p//c + r