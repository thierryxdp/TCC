import math
def colchao(medidas,H,L):
    a = math.sqrt((H**2) + (L**2))
    rel_b_c_l = medidas[2]*math.sqrt(2) + medidas[1]/math.sqrt(2)
    
    if medidas[1] < H and medidas[2] < L:
        return True
    if medidas[1] < a and L <= rel_b_c_l:
        return True
    else:
        return False