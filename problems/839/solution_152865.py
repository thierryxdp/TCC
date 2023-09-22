import math
def carros(pessoas,capacidade=5):
    """informara o numero de carros necessario baseado na 
    quantidade e pessoas que irao viajar e na capacidade
    do carro, caso nao sejam informados sera levado em consi
    deracao que a capcidade e cinco. int, int -> int """
    return math.ceil(pessoas/capacidade)