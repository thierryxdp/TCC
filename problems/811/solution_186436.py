def colchao(medidas,H,L):
    """função que calcula e retorna se um colchao passam por uma porta
    list, int, int ->  bool"""
    [a,b,c] = medidas
    if (b <= H) or (b <= L) or (c <= H) or (c <= L): 
        return True
    else:
        return False