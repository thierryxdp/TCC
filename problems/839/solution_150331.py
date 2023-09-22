def carros(x,y=5):
    if x%y ==0:
        return x//y
    else:
        return x//y+1
    """calcula e retorna o numero de carros necessários para a viagem, para x como numero de pessoas e y a capacidade do carro"""
    return x%y