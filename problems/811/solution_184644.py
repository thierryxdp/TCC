def colchao(medidas,H,L):
    '''determina se o colchao com dimensoes determinadas 
    pela lista medidas pode passar pela porta de altura
    H e largura L; list, int, int -> bool'''
    m1 = medidas[0]
    m2 = medidas[1]
    m3 = medidas[2]
    if H>m1 or H>m2 and L>m3:
        return True
    elif H>m2 or H>m3 and L>m1:
        return True
    elif H>m1 or H>m3 and L>m2:
        return True
    else:
        return False