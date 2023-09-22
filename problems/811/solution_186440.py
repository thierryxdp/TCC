def colchao(medidas,H,L):
    """Retorna um valor booleano indicando se o colchão passa pela porta:
    list,int,int-> bool"""
    [a,b,c] =  medidas
    if (b <= H or L) and (a<= L or H):
        return True
    
    else:
        return False