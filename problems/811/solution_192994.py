def colchao(c, h, l):
    """recebe as medidas do colchão e da porta e avalia se o colchao passa pela porta
    list + int + int -> bool"""
    if c[1] <= h or c[1] <= l:
        return True
    elif c[2] <= h or c[2]<= l:
        return True
    else:
        return False