import math

def bolos(farinha, ovos, leite):
    xicara = farinha / 2
    qtdOvos = ovos / 3
    colLeite = leite / 5
    
    if xicara < 2 or qtdOvos < 3 or colLeite < 5:
        return 0
    
    bololo = ((xicara + qtdOvos + colLeite)/3)
    return bololo