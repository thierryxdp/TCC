import math

def bolos(farinha, ovos, leite):
    xicaras = 2 / farinha
    qtdOvo = 3 / ovos
    colhleite = 5 / leite
    
    bololo = (xicaras + qtdOvos + colhleite)
    return math.floor(bololo)