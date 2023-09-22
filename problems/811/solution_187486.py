def colchao(medidas,H,L):
    '''funcao que dados os paremetros de entrada referentes as informacoes das medidas do colchao e da altura e largura de uma porta,
    retorna se e possivel atravessar o colchao pela porta
    list, int, int -> bool'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<=L and C<=H:
        return True 
    elif B<=L and C<=H:
        return True
    elif B<=L and A<=H:
        return True
    elif C<=L and A<=H:
        return True
    elif A<=L and B<=H:
        return True
    elif C<=L and B<=H:
        return True 
    else:
        return False