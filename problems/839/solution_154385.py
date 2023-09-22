def carros(pessoas, capacidade=5):
    """Calcula a qunatidade de carros em relaçao ao numero de pessoas
    int,int -> int"""
    import math.ceiling
    return pessoas//math.ceil(capacidade)