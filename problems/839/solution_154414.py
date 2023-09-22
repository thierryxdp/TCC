def carros(x, y=5):
    """Calcula o numero de veiculos necessários para atender a todos os passageiros dados o numero
    de passageiro e a capacidade do veiculo, se a capacidade não for informada ela é 5;
    int, int -> float"""
    if x==y:
        return x//y
    else:
        return x//y + 1