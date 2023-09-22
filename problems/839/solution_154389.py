def carros(pessoas, capacidade=5):
    """Calcula a qunatidade de carros em relaçao ao numero de pessoas
    int,int -> int"""
    import math 
    return math.ceil(pessoas//capacidade)