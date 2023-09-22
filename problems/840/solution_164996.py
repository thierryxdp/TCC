import math

def bolos(farinha, ovos, leite):
    xicara = 2 // farinha
    qtdOvos = 3 // ovos
    colLeite = 5 // leite
    
    if xicara < 2 or qtdOvos < 3 or colLeite < 5:
        return 0
    
    bololo = (xicara + qtdOvos + colLeite)
    return math.floor(bololo)