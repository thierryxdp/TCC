def colchao(medidas,H,L):
    A,B,C = medidas
    if min(medidas) > min(H,L):
        return False
    elif numero_meio > max(H,L):
    numero_meio = medidas.sort()[1]
        return False
    else:
        return True