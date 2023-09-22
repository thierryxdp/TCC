def colchao(medidas,h,l):
    """funcao que retorna True se o colchao passar pela porta, e False, caso
    contrario
    list,int,int->bool"""
    medidas.sort()
    if medidas[0] > h:
        if medidas[0] > l:
            return False
        elif medidas[1] > l:
            return False
        else:
            return True
    elif medidas[1] > h:
        return False
    else:
        return True