def bolos (A=2,B=3,C=5):
    import math
    'int, int, int -> int'
    if (A/2)<(B/3) and (A/2)<(C/5):
        return math.floor(A/2)
    elif (B/3)<(A/2) and (B/3)<(C/5):
        return math.floor(B/3)
    elif (C/5)<(A/2) and (C/5)<(B/3):
        return math.floor(C/5)