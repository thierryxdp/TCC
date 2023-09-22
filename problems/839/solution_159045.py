def carros (pessoas,capacidade=5):
    import math
    'Calcula a quantidade de carros necessária para levar uma quantidade de pessoas'
    'int, int -> int'
    return math.ceil(pessoas/capacidade)