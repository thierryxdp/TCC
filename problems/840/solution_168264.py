def bolos(A,B,C):
    if min(A,B,C)==A and A<2:
        return A/2
    if min(A,B,C)==B and B<3:
        return B/3
    if min(A,B,C)==C and C<5:
        return C/5
    else:
        return 0