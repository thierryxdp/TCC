def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<L:
        if C<H:
            return True
        else:
            return False