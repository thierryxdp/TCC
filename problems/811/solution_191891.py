def colchao(medidas,h,l):
    """retorna se um móvel passa em uma porta
   list,float,float->bool"""
    
    if min(medidas[1],medidas[2]) <= l or min(medidas[1],medidas[2]) <= h:
        return True
    
    else:
        return False