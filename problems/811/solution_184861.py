def colchao(medidas,H,L):
    '''função que dada as medidas retorna em booleano se ele consegue ou nao passar o colchao pela porta:'''
    A= lista[0]
    B= lista[1]
    
    if (B<=H and A<=L) or (B<=L and A<=H):
        return True
    else:
        return False