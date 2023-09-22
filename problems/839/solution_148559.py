def carros (p, c=5):
    "Calcula o numero de carros necessarios para a viagem"
    #c = capacidade do veiculo
    import math
    return math.ceil(p/c)