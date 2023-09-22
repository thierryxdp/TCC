def colchao(col, h, l):
    """recebe as dimensoes do colchão e da porta e avalia se o colchao passa pela porta
    list + int + int -> bool"""
    a, b, c = col
    if max(a,b, c) >= min(h,l):
        return True
    else:
        return False