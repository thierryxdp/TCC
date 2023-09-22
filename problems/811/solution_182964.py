def colchao(medidas,H,L):
    """função que informa se as dimensoes do colchao irao passar pela porta"""
    if (medidas[1]*medidas[2]<H*L) or (H*L>medidas[0]*medidas[2]):
        return True
    else:
        return False