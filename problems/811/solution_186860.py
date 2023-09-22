def colchao(medidas,H,L):
    if medidas[1:2] > [H] and medidas[2:] > [L]:
        return False
    if medidas[1:2] <= [H] and medidas[2:] > [L]:
        return True
    if medidas[1:2] > [H] and medidas[2:] < [L]:
        return True
    else:
        True