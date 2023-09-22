def bolos (A=2,B=3,C=5):
    import math
    'int, int, int -> int'
    if min (A,B,C) == A:
        return A/2
    elif min(A,B,C) == B:
        return B/3
    else:
        return C/5