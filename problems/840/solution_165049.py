def bolos(A,B,C):
    bolo = 0
    while (A >= 2 and B >= 3 and C>=5):
        bolo = bolo + 1
        A = A - 2
        B = B - 3
        C = C - 5
    return bolo