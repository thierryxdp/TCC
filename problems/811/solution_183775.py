def colchao(medidas,H,L):
    """função que informa se um colchão com medidas especififcadas pelo usuario passa por uma porta com medidas H e L"""
    """list,int,int->bool"""
    if medidas[1] <= H or medidas[1] <= L:
        return True
    else: 
        return False