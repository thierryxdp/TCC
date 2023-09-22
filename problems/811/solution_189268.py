def colchao(medidas,H,L):
    '''função que verifica se um colchão passa por uma porta, lista, int, int-> bool'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if(A>H or B>H or C>H):
        return False
    else:
        return True