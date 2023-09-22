def colchao(lista,H,L):
    """..."""

    A= lista[0]
    B= lista[1]

    if (A<=H and B<=L) or (B<=L and A<=H):
        return True
    else:
        return False