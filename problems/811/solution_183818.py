def colchao(medidas,H,L):
    a,b,c=medidas
    porta=[H,L]
    if (a<=H and b<=L) or (b<=H and a<=L):
        return True
    elif (b<=H and c<=L) or (c<=H and b<=L):
        return True
    elif (a<=H and c<=L) or (c<=H and a<=L):
        return True
    else:
        return False