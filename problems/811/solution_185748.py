def colchao(medidas, h, l):
    """ mostra se o colchão passa pela porta;
    list, int, int -> bool"""
    ac = medidas[0]
    cc = medidas[1]
    lc = medidas[2]
    if (cc>h):
        if (lc>l):
            return False
        else:
            return True
        if (lc<1):
            return True
        else:
            return True