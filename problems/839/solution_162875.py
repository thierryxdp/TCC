def carros(pes,cap):
    if pes%cap!=0:
        return math.ceil(pes/cap)
    else:
        return pes/cap