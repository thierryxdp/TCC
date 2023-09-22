#função que diz quantos carros são necessários
def carros(pes,cap=5):
    import math
    if pes<= 5:
        return 1
    else:
        return math.ceil(pes/cap)