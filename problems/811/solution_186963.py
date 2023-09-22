def colchao(medidas, H, L):
    """diz se o colchao passa pela porta ou nao.int->str."""
    #H é a altura da porta
    #L é a largura da porta
    #medidas são as dimensões do colchão(A,B,C)
    A, B, C = medidas
    if ((A<= H or L) and (B<= H or L)):
        return True
    if ((B<= H or L) and (C<= H or L)):
        return True
    if ((C<= H or L) and (A<= H or L)):
        return True
    else:
        return False