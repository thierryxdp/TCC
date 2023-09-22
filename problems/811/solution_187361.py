import math
def colchao(medidas,H,L):
    a = math.sqrt((H**2) + (L**2))
    b_max = math.sqrt((medidas[1]-(medidas[2]*math.sqrt(2)))**2 - (medidas[2]-(medidas[2]*math.sqrt(2)))**2)
    if medidas[1] < H and medidas[2] < L:
        return True
    if medidas[1] < a and medidas[1] <= b_max
    else:
        return False