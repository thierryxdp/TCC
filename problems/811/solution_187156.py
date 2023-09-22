def colchao(medidas,h,l):
    """aclcula e retorna se um colchão atravessa uma porta list,int,int->bool"""
    if int(medidas[0:1])<l and int(medidas[2:])<h:
        return True
    else:
        return False