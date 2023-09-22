def colchao(medidas,H,L):
    A,B,C = medidas
    meio = A,B,C.sort()
    meio1 = meio[1]
    if min(medidas) > min(H,L):
        return False
    elif meio1 > max(H,L):
        return False
    else:
        return True