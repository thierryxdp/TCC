def colchao(medidas,H,L):
    """Retorna um valor booleano indicando se o colchão passa pela porta:
    list,int,int-> bool"""
    [a,b,c] =  medidas
    if b<=L and a<=H:
    elif (b <= H) and (a<= L):
        return True
    else:
        return False