def carros(P,C=5):
    """função que calcula e retorna o número exato de carros para viagem com p número de passageiros e c a capacidade do veículo.Caso c não for informado será igual a 5
    int,int> float"""
    return math.ceil (P//C)