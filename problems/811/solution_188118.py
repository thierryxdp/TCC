def colchao (medidas,H,L):
    mat = medidas
    por = H,L
    if (mat[0] <= por[1] and mat[1] <= por[0]) or (mat[0] <= por[0] and mat[1] <= por[1]):
        return True
    else:
        return False