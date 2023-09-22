def bolos(a,b,c):
    A = a/2
    B = b/3
    C = c/5
    if a<2 or b<3 or c<4:
        return 0
    if a==2 or b==3 or c==5:
        return 1
    else:
        return int(min(A,B,C))