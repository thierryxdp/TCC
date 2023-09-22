def colchao(medidas,h,l):
    """calcula e retorna se um colchão atravessa uma porta list,int,int->bool"""
    if medidas[0:1]<[l] and medidas[1:2]<[h]:
        return True
    elif  medidas[0:1]<[h] and medidas[1:2]<[l]:
        return True
    elif  medidas[0:1]<[h] and medidas[2:]<l]:
        return True
    else:
        return False