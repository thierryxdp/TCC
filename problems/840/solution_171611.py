import math
def bolos(A,B,C)
	farinha= math.ceil(A/2)
    ovos= math.ceil(B/3)
    leite = math.ceil (C/5)
    return min(farinha,ovos,leite)