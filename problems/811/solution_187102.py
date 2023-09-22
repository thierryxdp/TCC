"""Retorna se o colchão passa ou não pela porta"""
def colchao(medidas,H,L):
    medidas=A,B,C
    if A and B <=H:
        return True
    if A and C<=H:
        return True
    if B and C<=H:
        return True
    if A and B<=L:
        return True
    if A and C<=L:
        return True
    if B and C<=L:
        return True
    else:
        return False