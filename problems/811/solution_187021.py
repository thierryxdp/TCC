def colchao(medidas, H, L):
    """diz se o colchao passa pela porta ou nao.int->str."""
    #H é a altura da porta
    #L é a largura da porta
    #medidas são as dimensões do colchão(A,B,C)
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if ((A>H and B>H) and (A>L and B>L)):
        return False
    if ((C>H and B>H) and (C>L and B>L)):
        return False
    if ((A>H and C>H) and (A>L and C>L)):
        return False
    else:
        return True