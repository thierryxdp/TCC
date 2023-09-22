def colchao(medidas,H,L):
    ''' '''
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    if a<=L and b<=H or a<=L and c<=H or b<=L and a<=H or b<=L and c<=H or c<=L and a<=H or c<=L and b<=H:
        return True
    else:
        return False