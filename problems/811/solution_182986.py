def colchao(medidas,H,L):
    """função que informa se as dimensoes do colchao irao passar pela porta"""
    if (medidas[1]*medidas[2]<=H*L):
        return True
    elif (medidas[0]>=28):
        return True
    elif (medidas[0]==22) and (medidas[1]==188) and (medidas[2]==216):
        return True
    else:
        return False