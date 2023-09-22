def bolos(A,B,C):
    if A//2>=1 and B//3>=1 and C//5>=1:
        return min(A//2,B//3,C//5)
    else:
        return 0