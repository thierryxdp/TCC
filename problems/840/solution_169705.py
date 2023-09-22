"""

int, int, int -> int
"""
import math
def bolos(A,B,C):
    x = A/2
    y = B/3
    z = C/5
    return math.min(x,y,z)