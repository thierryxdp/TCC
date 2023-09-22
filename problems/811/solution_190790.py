colchao(medidas,H,L):
HL = H*L
colchao1 = medidas[1]*medidas[2]*medidas[0]
    if colchao1 > HL:
        return False
    if colchao1 < HL:
        return True