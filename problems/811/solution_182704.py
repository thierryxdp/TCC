def colchao(medida,h,l):
    """Retorna se o colchão passará pela porta
    int, int, int, int, int -> bool"""
    
    if ((medida[0]>=h) and (medida[1]>=l)) or ((medida[0]>=l) and (medida[1]>=h)):
        return True
    elif ((medida[0]>=h) and (medida[2]>=l)) or ((medida[0]>=l) and (medida[2]>=h)):
        return True
    elif ((medida[2]>=h) and (medida[1]>=l)) or ((medida[2]>=l) and (medida[1]>=h)):
        return True
    else:
        return False