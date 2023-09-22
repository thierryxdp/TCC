def colchao(medidas,H,L):
    B=medidas[1:2]
    C=medidas[2:]
    if B<=[H] or B<=[L]:
        return True
    if C<=[H]or C<=[L]:
        return True
    else:
        return False