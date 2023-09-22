def colchao(medidas, H, L):
    """diz se o colchao passa pela porta ou nao.int->str."""
    #H é a altura da porta
    #L é a largura da porta
    #medidas são as dimensões do colchão(A,B,C)
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if ((A and B and C)>H or (A and B and C)>L):
        return False
    else:
        return True