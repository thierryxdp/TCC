def colchao(medidas,h,l):
    """Dado as medidas do colchão e da porta, fala se passa ou não. list,int,int>bol"""
    if medidas[1]<h or medidas[2]<l:
        return True
    else:
        return False