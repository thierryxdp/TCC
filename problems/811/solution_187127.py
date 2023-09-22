"""Retorna se o colchão passa ou não pela porta:
int,int,int->bool"""
aux=A
aux2=B
aux3=C
def colchao(medidas,H,L):
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