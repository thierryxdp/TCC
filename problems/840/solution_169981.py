def bolo(a,b,c):
    A= a/2
    B= b/3
    C= c/5
    if A == B == C:
        return A
    else:
        return min(A,B,C)