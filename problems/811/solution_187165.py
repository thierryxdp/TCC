def colchao(medidas,h,l):
    """aclcula e retorna se um colchão atravessa uma porta list,int,int->bool"""
    if medidas[0]<l medidas[2:]<h:
        return True
    else:
        return False