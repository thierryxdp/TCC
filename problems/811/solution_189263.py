def colchao(medidas,H,L):
    '''função que verifica se um colchão passa por uma porta, lista, int, int-> bool'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if(A*B>H or A*C>H or B*C>H or B>1900):
        return False
    else:
        return True