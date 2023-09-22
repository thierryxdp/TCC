def colchao(m,h,l):
    "retorna se o colchão passa ou não pela porta"
    m.sort()
    if m[0] > h:
        if m[0] > l:
            return False
        elif m[1] > l:
            return False
        else:
            return True
    elif m[1]>h:
        return False
    else:
        return True