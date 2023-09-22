def colchao(medidas,H,L):
    A,B,C = medidas
    meio = A,B,C.sort()[1]
    if min(medidas) > min(H,L):
        return False
    elif meio > max(H,L):
        return False
    else:
        return True