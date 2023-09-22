def colchao(m,h,l):
    '''funcao que retorna True se o colchao passar pela porta, e False, caso contrario'''
    m.sort ()
    if m[0] > h:
        if m[0] > l:
            return False
        elif m[1] > l:
            return False
        else:
            return True
    elif m[1] > h:
        return False
    if m[0] > l:
            return False
        elif m[1] > l:
            return Falseif m[0] > l:
            return False
        elif m[1] > l:
            return False
    else:
        return True