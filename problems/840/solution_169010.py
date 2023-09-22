import math

# int, int, int -> int
def bolos(A,B,C):
    return int( math.floor( min( A/2, B/3, C/5 ) ) )