def colchao(medidas,H,L):
    """d=AxBxC=lista com 3 elementos
    h,l=int"""
    if(((medidas[0]<=H)and(medidas[1]<=L)or(medidas[1]<=H))and(medidas[0]<=L)or((medidas[0]<=H)and(medidas[2]<=L)or(medidas[2]<=H)and(medidas[0]<=L))or((medidas[1]<=H)and(medidas[2]<=L)or(medidas[2]<=H)and(medidas[1]<=L))):
        return True
    else:
        return False