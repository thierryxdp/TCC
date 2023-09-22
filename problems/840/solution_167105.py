import math
def bolos(A,B,C):
    A=math.floor(A/2);
    B=math.floor(B/3);
    C=math.floor(C/5);
    return min(A,B,C)