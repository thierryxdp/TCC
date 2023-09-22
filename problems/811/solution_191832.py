def colchao(medidas,H,L):
    '''função em que dada uma lista (medidas) com as dimensões de um colchão
    em centímetros, da menor para a maior, e dois números inteiros
    correspondentes à altura e à largura da porta em
    centímetros, retorna se o colchão consegue passar ou não pela porta
    list, int, int -> bool'''
    P=medidas[0]
    l=medidas[1]
    A=medidas[2]
    if P<=H and l<=L:
        return True
    elif P<=H and A<=L:
        return True
    elif l<=H and A<=L:
        return True
    elif A<=H and l<=L:
        return True
    elif P<=L and A<=H:
        return True
    elif P<=L and l<=H:
        return True
    else:
        return False