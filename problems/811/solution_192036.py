def colchao(col, h, l):
    """recebe as dimensoes do colchão e da porta e avalia se o colchao passa pela porta
    list + int + int -> bool"""
    if col[1] <= (h or l):
        return True
    elif col[2] <= (h or l):
        return True
    else:
        return False