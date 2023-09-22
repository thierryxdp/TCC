def colchao(medidas,H,L):
    '''função que verifica se um colchão passa por uma porta, lista, int, int-> bool'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    '''frente'''
    if(A<=H or C<=H or B<=H):
        return True
    else:
        return False
    '''lado'''
    if(