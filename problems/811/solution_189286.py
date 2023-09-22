def colchao(medidas,H,L):
    '''função que verifica se um colchão passa por uma porta, lista, int, int-> bool'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]    
    if(B<=H or B<=L or C<=H and C<=L):
        return True
    else:
        return False