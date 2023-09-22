import math
def carros (pes, cap = 5):
    if  pes%cap !=0:
        return math.ceil(pes/cap)