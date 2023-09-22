import math

def bolos(farinha, ovos, leite):
    xicara = farinha // 2
    qtdOvos = ovos // 3
    colLeite = leite // 5
    
    if farinha < 2 or ovos < 3 or leite < 5:
        return 0
    if farinha ==2 or ovos == 3 or leite == 5:
        return 1
    bololo = ((xicara + qtdOvos + colLeite)/3)
    return math.floor(bololo)