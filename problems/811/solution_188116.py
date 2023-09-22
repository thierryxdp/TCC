def colchao (medidas,H,L):
    mat = medidas
    por = H,L
    if (mat[0] <= por[0] and mat[2] <= por[1]):
        return True
    else:
        return False