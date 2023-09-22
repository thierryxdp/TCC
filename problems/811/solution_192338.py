def colchao(medidas,H,L):
    """string int int -> tupla int int"""
    
    if int(medidas[1])<=H or int(medidas[2])<=L: 
        return True
    else:
        return False