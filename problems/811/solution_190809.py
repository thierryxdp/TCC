def colchao(dimensoes,H,L):
    A,B,C = dimensoes
    if C<=H and B<=L:
        return True
    elif C<=H and A<=L:
        return True
    elif A<=H and B<=L:
        return True
    elif B<=H and A<=L:
        return True
    elif C<=L and B<=H:
        return True
    elif C<=L and A<=H:
        return True
    else:
        return False