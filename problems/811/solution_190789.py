Cabe(colchao, H,L):
HL = H*L
colchao1 = colchao[1]*colchao[2]*colchao[0]
    if colchao1 > HL:
        return False
    if colchao1 < HL:
        return True