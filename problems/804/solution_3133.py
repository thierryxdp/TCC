def filtra_pares(tupla):
    """função que dada uma tupla com elementos retoma a uma nova tupla com os elementos pares da tupla original"""
    a,b,c,d= tupla
    if type(a)==par and type(b)==par and typr(c)==par and type(d)==par:
        return (a,b,c,d), ()
    if type(a)==par and type(b)==par and typ(c)==par and type(d)==impar:
        return (a,b,c), (d)
    if type(a)==par and type(b)==par and typ(c)==impar and type(d)==impar:
        return (a,b), (c,d)
    if type(a)==par and type(b)==impar and typ(c)==impar and type(d)==impar:
        return (a), (b,c,d)
    else:
        return (), (a,b,c,d)