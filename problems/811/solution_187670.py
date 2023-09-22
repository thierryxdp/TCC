"""Retorna se o colchão passa ou não pela porta:
int,int,int->bool"""
def colchao(A,B,C,H,L):
 	A, B, C= medidas
	if (A<H) and (B<H):
        return True
    if A<H and C<=H:
        return True
    if B<=H and C<=H:
        return True
    if A<=L and B<=L:
        return True
    if A<=L and C<=L:
        return True
    if B<=L and C<=L:
        return True
    else:
        return False