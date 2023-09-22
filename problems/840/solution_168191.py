import math
def bolos (A,B,C):
    A=math.ceil(A/2)
    B=math.ceil(B/3)
    C=math.ceil(C/5)
    if A<=B and B<=C:
        return A
    if B<=A and C<=B:
        return B
    elif return C