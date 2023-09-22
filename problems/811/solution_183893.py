def colchao(medidas,H,L):
    a = H
    b = L
    if H < L:
        a = L
        b = H
    if a > medidas[1] or b > medidas[0]:
        return False
    else:
        return True