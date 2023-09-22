def colchao(medidas,H,L):
    """verifique se um colchao passa por uma porta dada as medidas do colchao e da porta em cm
    medidas->dimensoes do colchao(AxBxC)
    H->altura da porta
    L->largura da porta
    lista,int,int->bool"""
    if medidas[0]<L and medidas[1]<H or medidas[3]<H and medidas[0]<L or medidas[1]<L and medidas[0]<H:
        return True
    else:
        return False