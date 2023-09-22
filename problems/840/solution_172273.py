import math

def bolos(A, B, C):
    resultado_A = A/2
    resultado_B = B/3
    resultado_C = C/5
    if resultado_A <=resultado_B and resultado_A <= resultado_C:
        return round(resultado_A)
    elif resultado_B <= resultado_A and resultado_B <= resultado_C:
        return round(resultado_B)
    else:
        return math.floor(resultado_C)