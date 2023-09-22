import math
def bolos(A,B,C):
    """função que indica a quantidade máxima de bolos
    que João consegue fazer com os ingredientes A, B e C dados."""
    return math.floor(((A/2)+(B/3)+(C/5))/3)