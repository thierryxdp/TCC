def colchao(medidas,H,L):
    '''
       A função recebe as medidas do colchao e da porta 
       e retorna True quando o colchao passa pela porta e
       False quando não é possível passar o colchao pela 
       porta
       list, int, int -> bool
    '''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if (A <= H and B <= L):
        return True
    elif (A <= H and C <= L):
        return True
    elif (B <= H and A <= L):
        return True
    elif (B <= H and C <= L):
        return True
    elif (C <= H and A <= L):
        return True 
    elif (C <= H and B <= L):
        return True
    else:
        return False