def colchao(medidas,H,L):
    """função que calcula e retorna se um colchao passam por uma porta
    list, int, int ->  bool"""
    medidas = [a,b,c]
    if c> H or L:
        return True
    else:
        return False