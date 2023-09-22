def bolos(A,B,C):
    if (A // 2) < (B // 3) and (A // 2) < (C // 5):
        return A // 2
    if (B // 3) < (A // 2) and (B // 3) < (C // 5):
        return B // 3
    if (C // 5) < (B // 3) and (C // 5) < (A // 2):
        return C // 5
    elif A // 2 == B // 3 == C // 5:
        return A // 2
    elif A // 2 == C // 5 and B != 0:
        return A // 2
    elif A // 2 == B // 3 and C != 0:
        return A // 2
    elif C // 5 == B // 3 and A != 0:
        return C // 5