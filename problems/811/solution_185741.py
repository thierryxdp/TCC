def colchao(medidas, h, l):
    """ mostra se o colchão passa pela porta;
    list, int, int -> bool"""
    ac = medidas[0]
    cc = medidas[1]
    lc = medidas[2]
    if cc>h:
        if lc>l:
            return False
        elif lc<l:
            return True
            else:
                return True