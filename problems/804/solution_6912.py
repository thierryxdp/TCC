def filtra_pares(p):
    """Função que retorna uma nova tupla apenas com elementos da tupla original, mantendo a ordem antiga."""
    """tupla, tupla --> int"""
	p1 = p[0]
    p2 = p[1]
    p3 = p[2]
    p4 = p[3]


    if((p[0]%2) == 0):
        a = 1
    else: a = 0
    if((p[1]%2) == 0):
        b = 1
    else: b = 0
    if((p[2]%2) == 0):
        c = 1
    else: c = 0
    if((p[3]%2) == 0):
        d = 1
    else: d = 0


    if((a == 1) and (b == 1) and (c == 1) and (d == 1)):
        return p1, p2, p3, p4
    if((a != 1) and (b == 1) and (c == 1) and (d == 1)):
        return p2, p3, p4
    if((a != 1) and (b != 1) and (c == 1) and (d == 1)):
        return p3, p4
    if((a != 1) and (b != 1) and (c != 1) and (d == 1)):
        return (p4,)
    if((a != 1) and (b != 1) and (c != 1) and (d != 1)):
        return ()
    if((a == 1) and (b != 1) and (c != 1) and (d != 1)):
        return (p1,)
    if((a != 1) and (b == 1) and (c != 1) and (d != 1)):
        return (p2,)
    if((a != 1) and (b != 1) and (c == 1) and (d != 1)):
        return (p3,)
    if((a == 1) and (b == 1) and (c != 1) and (d != 1)):
        return p1, p2
    if((a != 1) and (b == 1) and (c == 1) and (d != 1)):
        return p2, p3
    if((a == 1) and (b != 1) and (c != 1) and (d == 1)):
        return p1, p4
    if((a == 1) and (b != 1) and (c == 1) and (d != 1)):
        return p1, p3
    if((a != 1) and (b == 1) and (c != 1) and (d == 1)):
        return p2, p4
    if((a == 1) and (b != 1) and (c == 1) and (d == 1)):
        return p1, p3, p4
    if((a == 1) and (b == 1) and (c != 1) and (d == 1)):
        return p1, p2, p4
    if((a == 1) and (b == 1) and (c == 1) and (d != 1)):
        return p1, p2, p3