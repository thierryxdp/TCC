def colchao (medidas,H,L):
    mat = medidas
    por = H,L
    if mat[0] <= por[1] and mat[1] <= por[0]:
        return True
    else:
        return False