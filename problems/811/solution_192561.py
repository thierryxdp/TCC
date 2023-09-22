del colchao(medidas,H,L):
    '''Retorna True se o colchão de medidas=[a,b,c] consegue passar pela
    porta de dimensões H e L.'''
    if (medidas[0]<=L and medidas[1]<=H) or (medidas[0]<=H and medidas[1]<=L) or (medidas[1]<=L and medidas[2]<=H) or (medidas[1]<=H and medidas[2]<=L) or (medidas[0]<=L and medidas[2]<=H) (medidas[0]<=H and medidas[2]<=L):
        return True
    else:
        return False