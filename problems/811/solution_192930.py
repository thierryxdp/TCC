def colchao(m,h,l):
    "retorna se o colchão passa ou não pela porta"
    m.sort()
    if m[1] > h:
        if m[1] > l:
            return False
        elif m[2] > l:
            return False
        else:
            return True
    elif m[2]>h:
        return False
    else:
        return True