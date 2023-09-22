def colchao(medidas,H,L):
    '''funcao que recebe as dimensoes do colchao e as dimensoes da porta e determina se sera possivel passar o colchao pela porta'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    #Primeira forma
    if A<=L and C<=H:
        return bool(1)
    #Segunda forma
    elif A<=L and B<=H:
        return bool(1)
    #terceira forma
    elif C<=L and B<=H:
        return bool(1)
    #quarta forma
    elif C<=L and A<=H:
        return bool(1)
    else:
        return bool(0)