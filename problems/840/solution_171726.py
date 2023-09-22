def bolos(A,B,C):
    int(A=A/2)
    int(B=B/3)
    int(C=C/5)
    if A<2 and B<3 and C<5:
        return 0
    if A<=B and A<=C:
        return A
    if B<=A and B<=C:
        return B
    if C<=A and C<=B:
        return C