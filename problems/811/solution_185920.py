colchao(medidas,H,L):
    """ Diz se o colchão escolhido passa
    pela porta de dimensões H x L;
    list -> bool"""
    if medidas[0] and medidas[1] and medidas[2] > H:
        return False 
    elif medidas[0] and medidas[1] and medidas[2] > L:
        return False