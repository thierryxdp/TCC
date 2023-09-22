def porta (medidas,H,L):
    ''' Funcao que calcula qual lado exato de um colchao para passar pela porta; list,int, int -> bool''' 
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    if a<=H and b<=L:
        return True 
    if a<=H and c<=L:
        return True
    if b<=H and c<=L:
        return True
    if c<=H and b<=L:
        return True
    if a<=L and c<=H:
        return True
    if a<=L and b<=H:
        return True 
    else: 
        return False