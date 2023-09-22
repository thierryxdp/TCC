def colchao(medidas, H, L):
    """funcao que a partir das medidas do colchao ira descobrir se passa pela porta da casa de joao que tem altura H e largura L
    int,int,int -> bool"""
    if(medidas[1]<=H) or (medidas[2]<=H):
        return True
    elif(medidas[1]<=L) or (medidas[2]<=L):
        return True
    else:
        return False