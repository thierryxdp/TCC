def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<L:
        if C<H:
            return True
        elif B<H:
            return True
        else:
            return False
    elif A<H:
        if C<L:
            return True
        elif B<L:
            return True
        else: 
            return False
    elif A<L:
        if B<H:
            return True
        elif C<H:
            return True
        else:
            return False