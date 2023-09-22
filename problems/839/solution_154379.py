def carros(pessoas,capacidade=5):
    """Calcula a quantidade de carros necessarios para uma quantidade de pessoas
int, int -> int"""
    import math *
    return pessoas//math.ceil(capacidade)