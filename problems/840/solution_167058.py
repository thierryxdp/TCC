from math import floor
def bolos (A, B, C):
    return ((A + B + C)//10) - ((A//2 + B//3 + C//5)//3)