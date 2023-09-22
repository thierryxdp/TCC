def bolos(A,B,C):
    A=A/2
    B=B/3
    C=C/5
    if A<=B and A<=C:
        return A
    if B<=A and B<=C:
        return B
    else:
        return C