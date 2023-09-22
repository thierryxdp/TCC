def colchao(medidas,H,L):
    """dada as dimensoes do colchao e da porta, retorna se é possivel que este passe pela porta
    Dc:dimensoes do colchao
    Dp:dimensoes da porta"""
    if medidas[1]>H and medidas[2]>H and L<medidas[1] and L<medidas[2]:
        return False
    elif L>medidas[1] or L.medidas[2]:
        return True
    else:
        return True