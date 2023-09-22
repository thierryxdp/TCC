def colchao(medidas,H,L):
    """ """
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A>=B and A>=C:
        if B<=H and C<=L:
            return True
        elif C<=H and B<=L:
            return True
        else:
            return False
    elif B>=A and B>=C:
        if A<=H and C<=L:
        	return True
        elif C<=H and A<=L:
            return True
        else:
            return False
        
    else:
        if A<=H and B<=L:
        	return True
        elif B<=H and A<=L:
            return True
        else:
            return False