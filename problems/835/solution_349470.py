import math
def melhor_volta(tempos):
    """..."""
    t = (0,math.inf,0)
    for i in range(6):
        for j in range(10):
            if tempos[i][j] < t[1]:
                 t = (i+1,tempos[i][j],j+1) 
    return t