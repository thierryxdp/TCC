def colchao(medidas,H,L):
    '''função que recebe uma lista com as dimensões de um colchão e retorna
    o determinado colchão vai passar ou não pela porta; list,int,int->bolean'''
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