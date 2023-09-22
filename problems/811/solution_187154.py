def colchao(medidas,H,L):
    A,B,C = medidas
    if min(medidas) > min(H,L):
        return False
    elif meio > max(H,L):
        meio = A,B,C
    else:
        return True