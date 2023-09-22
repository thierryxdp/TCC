def carros (pessoas,capacidade=5):
    """int, int -> int"""
    from math import ceil
    return math.ceil(pessoas/capacidade)