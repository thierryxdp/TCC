def colchao(medidas,H,L):
    
    A=medidas[0:1]
    B=medidas[2:5]
    C=medidas[6:9]
    if A<H or A<L:
        return True
    if B<H or B<L:
        return True
    if C<H or C<L:
        return True
    else:
        return False