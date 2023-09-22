def colchao(medidas,H,L):
    '''
       função que retorna True se o colchão (medidas=[A,B,C])
       passa pela porta (altura H e largura L) e false caso 
       contrário
       list,int,int->bool
    '''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if (A<=H and A<=L) and (B<=H or B<=L):
        return True
    else:
        return False