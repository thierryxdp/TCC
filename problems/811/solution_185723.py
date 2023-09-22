def colchao(medidas, h, l):
    """ Mostra se o colcão passa pela porta;
    list, int, int -> bool"""
    ac = medidas[0]
    cc = medidas[1]
    lc = medidas[2]
    if cc > h:
        if lc > l:
            return False
        elif cc < h:
            if lc < l:
            return True
        elif lc < l:
            return True
        else:
            return True