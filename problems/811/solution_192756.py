def colchao(medidas,H,L):
    '''recebe uma lista com as medidas do colchão, a altura H e largura L da porta por onde ele deve passar 
    e retorna se o colchão passa pelas portas ou não através de valores booleanos True or False respectivamente 
    list, float, float -> bool''' 
    if medidas[0]<=H and medidas[1]<=L:
        return True 
    elif medidas[1]<=H and medidas[0]<=L:
        return True 
    elif medidas[0]<=L and medidas[2]<=H:
        return True 
    elif medidas[1]<=L and medidas[2]<=H:
        return True 
    else:
        return False