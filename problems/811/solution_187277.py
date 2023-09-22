def colchao(m,h,l):
    '''funcao que retorna True se o colchao passar pela porta, e False, caso contrario'''
    m.sort ()
    if m[0] > h:
        if m[0] > l:
            return false
        elif m[1] > l:
            return false
        else:
            return true
    elif m[1] > h:
        return false
    else:
        return true