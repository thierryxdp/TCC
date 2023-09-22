def colchao(medidas,H,L):
    '''função que verifica se um colchão passa por uma porta, lista, int, int-> bool'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    '''frente'''
    if(B<=H and B<=L or C<=H and C<=L):
        return True
    else:
        return False