import mach
def bolos(f,o,l):
    """função que calcula a quantidade maxima de bolos que ele consegue fazer"""
    return math.max(f//2,o//3,math.int(l/5))