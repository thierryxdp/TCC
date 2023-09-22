def filtra_pares(t):
    """."""
    nova_tupla = ()
    t1 = (t[0],)
    t2 = (t[1],)
    t3 = (t[2],)
    t4 = (t[3],)
    if (t[0] % 2)== 0:
        return nova_tupla + t1
    elif (t[1] % 2)== 0:
        return nova_tupla + t2 +t1
    elif (t[2] % 2)== 0:
        return nova_tupla + t3 + t2 + t3
    elif (t[3] % 2)== 0:
        return nova_tupla + t4 + t3 + t2 +t1