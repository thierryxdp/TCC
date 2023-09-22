def carros(p,c=5):
    """Calcula o número exato de veículos necessários para a viagem, dado o número de pessoas p e a capacidade de transporte c, caso o valor de c não seja inserido, será considerado a capacidade de 5 pessoas."""
    import math
    return math.ceil(p//c)