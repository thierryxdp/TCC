def x(A):
    return A//2
def y(B):
    return B//3
def z(C):
    return C//5
def bolos(A,B,C):
    min = x(A)
    if y(B) < min:
        min = y(B)
    if z(C) < min:
        min = z(C)
    return min