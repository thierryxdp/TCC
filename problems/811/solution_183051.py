def colchao(medidas,H,L):
    '''list,int,int -> bool'''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if (A<=H and B<=L) or (A<=H and C<=L) or (B<=H and A<=L) or (B,=H and C<=L) or (C<=H and A<=L) or (C<=H and A<=L):
        return True
    else:
        return False