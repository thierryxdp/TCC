import math

def bolos(farinha, ovos, leite):
    xicara = farinha // 2
    qtdOvos = ovos // 3
    colLeite = leite // 5
    
    qtdMin = math.min(xicara,qtdOvos,colLeite)
    return math.floor(qtdMin)