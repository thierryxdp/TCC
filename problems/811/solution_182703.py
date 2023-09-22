def colchao(a,b,c,h,l):
    """Retorna se o colchão passará pela porta
    int, int, int, int, int -> bool"""
    
    if ((a>=h) and (b>=l)) or ((a>=l) and (b>=h)):
        return True
    elif ((a>=h) and (c>=l)) or ((a>=l) and (c>=h)):
        return True
    elif ((c>=h) and (b>=l)) or ((c>=l) and (b>=h)):
        return True
    else:
        return False