def colchao(medidas,H,L):
    ''' Função que irá receber uma lista com as medidas de um
    colchão e verificar com as medidas também dadas da porta,
    se o colchão passará pela porta ou não, se passar a função
    deve retornar True, se não deve retornar False;
    list, int, int -> bool'''
    
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if A<=H and B<=L:
        return True
    elif A<=H and C<=L:
        return True
    elif B<=H and C<=L:
        return True
    elif C<=H and B<=L:
        return True
    elif A<=L and C<=H:
        return True
    elif A<=L and B<=H:
        return True
    else:
        return False