def colchao(medidas,H,L):
    """Retorna um valor booleano indicando se o colchão passa pela porta:
    list,int,int-> bool"""
    [a,b,c] =  medidas
    if b <= H and a<= L:
        return True
    else:
        return False