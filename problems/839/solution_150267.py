def carros(p, v=5):
    """o número de carros necessário para transportar um numero p de passageiros. int, int -> int"""
    return math.ceil(p/v)