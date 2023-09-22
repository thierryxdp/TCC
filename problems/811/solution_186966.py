def colchao(medidas, H, L):
    """diz se o colchao passa pela porta ou nao.int->str."""
    #H é a altura da porta
    #L é a largura da porta
    #medidas são as dimensões do colchão(A,B,C)
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if not((A<= H or L) and (B<= H or L)):
        return False
    if not((B<= H or L) and (C<= H or L)):
        return False
    if not((C<= H or L) and (A<= H or L)):
        return False
    else:
        return True