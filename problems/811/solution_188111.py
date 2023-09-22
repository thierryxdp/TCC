def colchao (medidas,H,L):
    mat = medidas
    por = H,L
    if mat[1] <= por[0] and mat[2] <= por[1]:
        return True
    else:
        return False